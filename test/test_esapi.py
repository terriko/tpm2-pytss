#!/usr/bin/python3 -u
"""
SPDX-License-Identifier: BSD-3
"""

import unittest

from tpm2_pytss import *
from .TSS2_BaseTest import TSS2_EsapiTest


class TestEsys(TSS2_EsapiTest):
    def testGetRandom(self):
        r = self.ectx.GetRandom(5)
        self.assertEqual(len(r), 5)

    def testCreatePrimary(self):
        inSensitive = TPM2B_SENSITIVE_CREATE()
        inPublic = TPM2B_PUBLIC()
        outsideInfo = TPM2B_DATA()
        creationPCR = TPML_PCR_SELECTION()

        inPublic.publicArea.type = TPM2_ALG.ECC
        inPublic.publicArea.nameAlg = TPM2_ALG.SHA1
        inPublic.publicArea.objectAttributes = (
            TPMA_OBJECT.USERWITHAUTH
            | TPMA_OBJECT.SIGN_ENCRYPT
            | TPMA_OBJECT.RESTRICTED
            | TPMA_OBJECT.FIXEDTPM
            | TPMA_OBJECT.FIXEDPARENT
            | TPMA_OBJECT.SENSITIVEDATAORIGIN
        )

        inPublic.publicArea.parameters.eccDetail.scheme.scheme = TPM2_ALG.ECDSA
        inPublic.publicArea.parameters.eccDetail.scheme.details.ecdsa.hashAlg = (
            TPM2_ALG.SHA256
        )
        inPublic.publicArea.parameters.eccDetail.symmetric.algorithm = TPM2_ALG.NULL
        inPublic.publicArea.parameters.eccDetail.kdf.scheme = TPM2_ALG.NULL
        inPublic.publicArea.parameters.eccDetail.curveID = TPM2_ECC.NIST_P256

        self.ectx.setAuth(ESYS_TR.OWNER, "")

        x, _, _, _, _ = self.ectx.CreatePrimary(
            ESYS_TR.OWNER,
            inSensitive,
            inPublic,
            outsideInfo,
            creationPCR,
            session1=ESYS_TR.PASSWORD,
        )
        self.assertIsNot(x, None)

    def testPCRRead(self):

        pcrsels = TPML_PCR_SELECTION.parse("sha1:3+sha256:all")
        _, _, digests, = self.ectx.PCR_Read(pcrsels)

        self.assertEqual(len(digests[0]), 20)

        for d in digests[1:]:
            self.assertEqual(len(d), 32)

    def test_plain_NV_define_write_read_undefine(self):

        nv_public = TPM2B_NV_PUBLIC(
            nvPublic=TPMS_NV_PUBLIC(
                nvIndex=TPM2_HC.NV_INDEX_FIRST,
                nameAlg=TPM2_ALG.SHA256,
                attributes=TPMA_NV.parse("ownerread|ownerwrite|authread|authwrite"),
                dataSize=32,
            )
        )

        # No password NV index
        nv_index = self.ectx.NV_DefineSpace(ESYS_TR.OWNER, None, nv_public)
        self.ectx.NV_Write(nv_index, b"hello world")

        value = self.ectx.NV_Read(nv_index, 11)
        self.assertEqual(value, b"hello world")

        public, name = self.ectx.NV_ReadPublic(nv_index)
        self.assertEqual(public.nvPublic.nvIndex, TPM2_HC.NV_INDEX_FIRST)
        self.assertEqual(public.nvPublic.nameAlg, TPM2_ALG.SHA256)
        self.assertEqual(
            public.nvPublic.attributes,
            TPMA_NV.parse("ownerread|ownerwrite|authread|authwrite|written"),
        )
        self.assertEqual(public.nvPublic.authPolicy.size, 0)
        self.assertEqual(public.nvPublic.dataSize, 32)
        # Algorithm id (UINT16) followed by SHA256 len of name bytes
        self.assertEqual(len(name), 2 + 32)

        n = str(name)
        self.assertEqual(len(n), 68)
        self.assertTrue(isinstance(n, str))

        self.ectx.NV_UndefineSpace(ESYS_TR.OWNER, nv_index)

        with self.assertRaises(TSS2_Exception):
            public, name = self.ectx.NV_ReadPublic(nv_index)


if __name__ == "__main__":
    unittest.main()