from ._libtpm2_pytss import lib, ffi


class TSS2_Exception(RuntimeError):
    RC_LAYER_SHIFT = lib.TSS2_RC_LAYER_SHIFT
    RC_LAYER_MASK = lib.TSS2_RC_LAYER_MASK
    TPM_RC_LAYER = lib.TSS2_TPM_RC_LAYER
    FEATURE_RC_LAYER = lib.TSS2_FEATURE_RC_LAYER
    ESAPI_RC_LAYER = lib.TSS2_ESAPI_RC_LAYER
    SYS_RC_LAYER = lib.TSS2_SYS_RC_LAYER
    MU_RC_LAYER = lib.TSS2_MU_RC_LAYER
    TCTI_RC_LAYER = lib.TSS2_TCTI_RC_LAYER
    RESMGR_RC_LAYER = lib.TSS2_RESMGR_RC_LAYER
    RESMGR_TPM_RC_LAYER = lib.TSS2_RESMGR_TPM_RC_LAYER
    BASE_RC_GENERAL_FAILURE = lib.TSS2_BASE_RC_GENERAL_FAILURE
    BASE_RC_NOT_IMPLEMENTED = lib.TSS2_BASE_RC_NOT_IMPLEMENTED
    BASE_RC_BAD_CONTEXT = lib.TSS2_BASE_RC_BAD_CONTEXT
    BASE_RC_ABI_MISMATCH = lib.TSS2_BASE_RC_ABI_MISMATCH
    BASE_RC_BAD_REFERENCE = lib.TSS2_BASE_RC_BAD_REFERENCE
    BASE_RC_INSUFFICIENT_BUFFER = lib.TSS2_BASE_RC_INSUFFICIENT_BUFFER
    BASE_RC_BAD_SEQUENCE = lib.TSS2_BASE_RC_BAD_SEQUENCE
    BASE_RC_NO_CONNECTION = lib.TSS2_BASE_RC_NO_CONNECTION
    BASE_RC_TRY_AGAIN = lib.TSS2_BASE_RC_TRY_AGAIN
    BASE_RC_IO_ERROR = lib.TSS2_BASE_RC_IO_ERROR
    BASE_RC_BAD_VALUE = lib.TSS2_BASE_RC_BAD_VALUE
    BASE_RC_NOT_PERMITTED = lib.TSS2_BASE_RC_NOT_PERMITTED
    BASE_RC_INVALID_SESSIONS = lib.TSS2_BASE_RC_INVALID_SESSIONS
    BASE_RC_NO_DECRYPT_PARAM = lib.TSS2_BASE_RC_NO_DECRYPT_PARAM
    BASE_RC_NO_ENCRYPT_PARAM = lib.TSS2_BASE_RC_NO_ENCRYPT_PARAM
    BASE_RC_BAD_SIZE = lib.TSS2_BASE_RC_BAD_SIZE
    BASE_RC_MALFORMED_RESPONSE = lib.TSS2_BASE_RC_MALFORMED_RESPONSE
    BASE_RC_INSUFFICIENT_CONTEXT = lib.TSS2_BASE_RC_INSUFFICIENT_CONTEXT
    BASE_RC_INSUFFICIENT_RESPONSE = lib.TSS2_BASE_RC_INSUFFICIENT_RESPONSE
    BASE_RC_INCOMPATIBLE_TCTI = lib.TSS2_BASE_RC_INCOMPATIBLE_TCTI
    BASE_RC_NOT_SUPPORTED = lib.TSS2_BASE_RC_NOT_SUPPORTED
    BASE_RC_BAD_TCTI_STRUCTURE = lib.TSS2_BASE_RC_BAD_TCTI_STRUCTURE
    BASE_RC_MEMORY = lib.TSS2_BASE_RC_MEMORY
    BASE_RC_BAD_TR = lib.TSS2_BASE_RC_BAD_TR
    BASE_RC_MULTIPLE_DECRYPT_SESSIONS = lib.TSS2_BASE_RC_MULTIPLE_DECRYPT_SESSIONS
    BASE_RC_MULTIPLE_ENCRYPT_SESSIONS = lib.TSS2_BASE_RC_MULTIPLE_ENCRYPT_SESSIONS
    BASE_RC_RSP_AUTH_FAILED = lib.TSS2_BASE_RC_RSP_AUTH_FAILED
    BASE_RC_NO_CONFIG = lib.TSS2_BASE_RC_NO_CONFIG
    BASE_RC_BAD_PATH = lib.TSS2_BASE_RC_BAD_PATH
    BASE_RC_NOT_DELETABLE = lib.TSS2_BASE_RC_NOT_DELETABLE
    BASE_RC_PATH_ALREADY_EXISTS = lib.TSS2_BASE_RC_PATH_ALREADY_EXISTS
    BASE_RC_KEY_NOT_FOUND = lib.TSS2_BASE_RC_KEY_NOT_FOUND
    BASE_RC_SIGNATURE_VERIFICATION_FAILED = (
        lib.TSS2_BASE_RC_SIGNATURE_VERIFICATION_FAILED
    )
    BASE_RC_HASH_MISMATCH = lib.TSS2_BASE_RC_HASH_MISMATCH
    BASE_RC_KEY_NOT_DUPLICABLE = lib.TSS2_BASE_RC_KEY_NOT_DUPLICABLE
    BASE_RC_PATH_NOT_FOUND = lib.TSS2_BASE_RC_PATH_NOT_FOUND
    BASE_RC_NO_CERT = lib.TSS2_BASE_RC_NO_CERT
    BASE_RC_NO_PCR = lib.TSS2_BASE_RC_NO_PCR
    BASE_RC_PCR_NOT_RESETTABLE = lib.TSS2_BASE_RC_PCR_NOT_RESETTABLE
    BASE_RC_BAD_TEMPLATE = lib.TSS2_BASE_RC_BAD_TEMPLATE
    BASE_RC_AUTHORIZATION_FAILED = lib.TSS2_BASE_RC_AUTHORIZATION_FAILED
    BASE_RC_AUTHORIZATION_UNKNOWN = lib.TSS2_BASE_RC_AUTHORIZATION_UNKNOWN
    BASE_RC_NV_NOT_READABLE = lib.TSS2_BASE_RC_NV_NOT_READABLE
    BASE_RC_NV_TOO_SMALL = lib.TSS2_BASE_RC_NV_TOO_SMALL
    BASE_RC_NV_NOT_WRITEABLE = lib.TSS2_BASE_RC_NV_NOT_WRITEABLE
    BASE_RC_POLICY_UNKNOWN = lib.TSS2_BASE_RC_POLICY_UNKNOWN
    BASE_RC_NV_WRONG_TYPE = lib.TSS2_BASE_RC_NV_WRONG_TYPE
    BASE_RC_NAME_ALREADY_EXISTS = lib.TSS2_BASE_RC_NAME_ALREADY_EXISTS
    BASE_RC_NO_TPM = lib.TSS2_BASE_RC_NO_TPM
    BASE_RC_BAD_KEY = lib.TSS2_BASE_RC_BAD_KEY
    BASE_RC_NO_HANDLE = lib.TSS2_BASE_RC_NO_HANDLE
    BASE_RC_NOT_PROVISIONED = lib.TSS2_BASE_RC_NOT_PROVISIONED
    BASE_RC_ALREADY_PROVISIONED = lib.TSS2_BASE_RC_ALREADY_PROVISIONED
    LAYER_IMPLEMENTATION_SPECIFIC_OFFSET = lib.TSS2_LAYER_IMPLEMENTATION_SPECIFIC_OFFSET
    LEVEL_IMPLEMENTATION_SPECIFIC_SHIFT = lib.TSS2_LEVEL_IMPLEMENTATION_SPECIFIC_SHIFT
    RC_SUCCESS = lib.TSS2_RC_SUCCESS
    TCTI_RC_GENERAL_FAILURE = lib.TSS2_TCTI_RC_GENERAL_FAILURE
    TCTI_RC_NOT_IMPLEMENTED = lib.TSS2_TCTI_RC_NOT_IMPLEMENTED
    TCTI_RC_BAD_CONTEXT = lib.TSS2_TCTI_RC_BAD_CONTEXT
    TCTI_RC_ABI_MISMATCH = lib.TSS2_TCTI_RC_ABI_MISMATCH
    TCTI_RC_BAD_REFERENCE = lib.TSS2_TCTI_RC_BAD_REFERENCE
    TCTI_RC_INSUFFICIENT_BUFFER = lib.TSS2_TCTI_RC_INSUFFICIENT_BUFFER
    TCTI_RC_BAD_SEQUENCE = lib.TSS2_TCTI_RC_BAD_SEQUENCE
    TCTI_RC_NO_CONNECTION = lib.TSS2_TCTI_RC_NO_CONNECTION
    TCTI_RC_TRY_AGAIN = lib.TSS2_TCTI_RC_TRY_AGAIN
    TCTI_RC_IO_ERROR = lib.TSS2_TCTI_RC_IO_ERROR
    TCTI_RC_BAD_VALUE = lib.TSS2_TCTI_RC_BAD_VALUE
    TCTI_RC_NOT_PERMITTED = lib.TSS2_TCTI_RC_NOT_PERMITTED
    TCTI_RC_MALFORMED_RESPONSE = lib.TSS2_TCTI_RC_MALFORMED_RESPONSE
    TCTI_RC_NOT_SUPPORTED = lib.TSS2_TCTI_RC_NOT_SUPPORTED
    TCTI_RC_MEMORY = lib.TSS2_TCTI_RC_MEMORY
    SYS_RC_GENERAL_FAILURE = lib.TSS2_SYS_RC_GENERAL_FAILURE
    SYS_RC_ABI_MISMATCH = lib.TSS2_SYS_RC_ABI_MISMATCH
    SYS_RC_BAD_REFERENCE = lib.TSS2_SYS_RC_BAD_REFERENCE
    SYS_RC_INSUFFICIENT_BUFFER = lib.TSS2_SYS_RC_INSUFFICIENT_BUFFER
    SYS_RC_BAD_SEQUENCE = lib.TSS2_SYS_RC_BAD_SEQUENCE
    SYS_RC_BAD_VALUE = lib.TSS2_SYS_RC_BAD_VALUE
    SYS_RC_INVALID_SESSIONS = lib.TSS2_SYS_RC_INVALID_SESSIONS
    SYS_RC_NO_DECRYPT_PARAM = lib.TSS2_SYS_RC_NO_DECRYPT_PARAM
    SYS_RC_NO_ENCRYPT_PARAM = lib.TSS2_SYS_RC_NO_ENCRYPT_PARAM
    SYS_RC_BAD_SIZE = lib.TSS2_SYS_RC_BAD_SIZE
    SYS_RC_MALFORMED_RESPONSE = lib.TSS2_SYS_RC_MALFORMED_RESPONSE
    SYS_RC_INSUFFICIENT_CONTEXT = lib.TSS2_SYS_RC_INSUFFICIENT_CONTEXT
    SYS_RC_INSUFFICIENT_RESPONSE = lib.TSS2_SYS_RC_INSUFFICIENT_RESPONSE
    SYS_RC_INCOMPATIBLE_TCTI = lib.TSS2_SYS_RC_INCOMPATIBLE_TCTI
    SYS_RC_BAD_TCTI_STRUCTURE = lib.TSS2_SYS_RC_BAD_TCTI_STRUCTURE
    MU_RC_GENERAL_FAILURE = lib.TSS2_MU_RC_GENERAL_FAILURE
    MU_RC_BAD_REFERENCE = lib.TSS2_MU_RC_BAD_REFERENCE
    MU_RC_BAD_SIZE = lib.TSS2_MU_RC_BAD_SIZE
    MU_RC_BAD_VALUE = lib.TSS2_MU_RC_BAD_VALUE
    MU_RC_INSUFFICIENT_BUFFER = lib.TSS2_MU_RC_INSUFFICIENT_BUFFER
    ESYS_RC_GENERAL_FAILURE = lib.TSS2_ESYS_RC_GENERAL_FAILURE
    ESYS_RC_NOT_IMPLEMENTED = lib.TSS2_ESYS_RC_NOT_IMPLEMENTED
    ESYS_RC_ABI_MISMATCH = lib.TSS2_ESYS_RC_ABI_MISMATCH
    ESYS_RC_BAD_REFERENCE = lib.TSS2_ESYS_RC_BAD_REFERENCE
    ESYS_RC_INSUFFICIENT_BUFFER = lib.TSS2_ESYS_RC_INSUFFICIENT_BUFFER
    ESYS_RC_BAD_SEQUENCE = lib.TSS2_ESYS_RC_BAD_SEQUENCE
    ESYS_RC_INVALID_SESSIONS = lib.TSS2_ESYS_RC_INVALID_SESSIONS
    ESYS_RC_TRY_AGAIN = lib.TSS2_ESYS_RC_TRY_AGAIN
    ESYS_RC_IO_ERROR = lib.TSS2_ESYS_RC_IO_ERROR
    ESYS_RC_BAD_VALUE = lib.TSS2_ESYS_RC_BAD_VALUE
    ESYS_RC_NO_DECRYPT_PARAM = lib.TSS2_ESYS_RC_NO_DECRYPT_PARAM
    ESYS_RC_NO_ENCRYPT_PARAM = lib.TSS2_ESYS_RC_NO_ENCRYPT_PARAM
    ESYS_RC_BAD_SIZE = lib.TSS2_ESYS_RC_BAD_SIZE
    ESYS_RC_MALFORMED_RESPONSE = lib.TSS2_ESYS_RC_MALFORMED_RESPONSE
    ESYS_RC_INSUFFICIENT_CONTEXT = lib.TSS2_ESYS_RC_INSUFFICIENT_CONTEXT
    ESYS_RC_INSUFFICIENT_RESPONSE = lib.TSS2_ESYS_RC_INSUFFICIENT_RESPONSE
    ESYS_RC_INCOMPATIBLE_TCTI = lib.TSS2_ESYS_RC_INCOMPATIBLE_TCTI
    ESYS_RC_BAD_TCTI_STRUCTURE = lib.TSS2_ESYS_RC_BAD_TCTI_STRUCTURE
    ESYS_RC_MEMORY = lib.TSS2_ESYS_RC_MEMORY
    ESYS_RC_BAD_TR = lib.TSS2_ESYS_RC_BAD_TR
    ESYS_RC_MULTIPLE_DECRYPT_SESSIONS = lib.TSS2_ESYS_RC_MULTIPLE_DECRYPT_SESSIONS
    ESYS_RC_MULTIPLE_ENCRYPT_SESSIONS = lib.TSS2_ESYS_RC_MULTIPLE_ENCRYPT_SESSIONS
    ESYS_RC_RSP_AUTH_FAILED = lib.TSS2_ESYS_RC_RSP_AUTH_FAILED
    FAPI_RC_GENERAL_FAILURE = lib.TSS2_FAPI_RC_GENERAL_FAILURE
    FAPI_RC_NOT_IMPLEMENTED = lib.TSS2_FAPI_RC_NOT_IMPLEMENTED
    FAPI_RC_BAD_REFERENCE = lib.TSS2_FAPI_RC_BAD_REFERENCE
    FAPI_RC_BAD_SEQUENCE = lib.TSS2_FAPI_RC_BAD_SEQUENCE
    FAPI_RC_IO_ERROR = lib.TSS2_FAPI_RC_IO_ERROR
    FAPI_RC_BAD_VALUE = lib.TSS2_FAPI_RC_BAD_VALUE
    FAPI_RC_NO_DECRYPT_PARAM = lib.TSS2_FAPI_RC_NO_DECRYPT_PARAM
    FAPI_RC_NO_ENCRYPT_PARAM = lib.TSS2_FAPI_RC_NO_ENCRYPT_PARAM
    FAPI_RC_MEMORY = lib.TSS2_FAPI_RC_MEMORY
    FAPI_RC_BAD_CONTEXT = lib.TSS2_FAPI_RC_BAD_CONTEXT
    FAPI_RC_NO_CONFIG = lib.TSS2_FAPI_RC_NO_CONFIG
    FAPI_RC_BAD_PATH = lib.TSS2_FAPI_RC_BAD_PATH
    FAPI_RC_NOT_DELETABLE = lib.TSS2_FAPI_RC_NOT_DELETABLE
    FAPI_RC_PATH_ALREADY_EXISTS = lib.TSS2_FAPI_RC_PATH_ALREADY_EXISTS
    FAPI_RC_KEY_NOT_FOUND = lib.TSS2_FAPI_RC_KEY_NOT_FOUND
    FAPI_RC_SIGNATURE_VERIFICATION_FAILED = (
        lib.TSS2_FAPI_RC_SIGNATURE_VERIFICATION_FAILED
    )
    FAPI_RC_HASH_MISMATCH = lib.TSS2_FAPI_RC_HASH_MISMATCH
    FAPI_RC_KEY_NOT_DUPLICABLE = lib.TSS2_FAPI_RC_KEY_NOT_DUPLICABLE
    FAPI_RC_PATH_NOT_FOUND = lib.TSS2_FAPI_RC_PATH_NOT_FOUND
    FAPI_RC_NO_CERT = lib.TSS2_FAPI_RC_NO_CERT
    FAPI_RC_NO_PCR = lib.TSS2_FAPI_RC_NO_PCR
    FAPI_RC_PCR_NOT_RESETTABLE = lib.TSS2_FAPI_RC_PCR_NOT_RESETTABLE
    FAPI_RC_BAD_TEMPLATE = lib.TSS2_FAPI_RC_BAD_TEMPLATE
    FAPI_RC_AUTHORIZATION_FAILED = lib.TSS2_FAPI_RC_AUTHORIZATION_FAILED
    FAPI_RC_AUTHORIZATION_UNKNOWN = lib.TSS2_FAPI_RC_AUTHORIZATION_UNKNOWN
    FAPI_RC_NV_NOT_READABLE = lib.TSS2_FAPI_RC_NV_NOT_READABLE
    FAPI_RC_NV_TOO_SMALL = lib.TSS2_FAPI_RC_NV_TOO_SMALL
    FAPI_RC_NV_NOT_WRITEABLE = lib.TSS2_FAPI_RC_NV_NOT_WRITEABLE
    FAPI_RC_POLICY_UNKNOWN = lib.TSS2_FAPI_RC_POLICY_UNKNOWN
    FAPI_RC_NV_WRONG_TYPE = lib.TSS2_FAPI_RC_NV_WRONG_TYPE
    FAPI_RC_NAME_ALREADY_EXISTS = lib.TSS2_FAPI_RC_NAME_ALREADY_EXISTS
    FAPI_RC_NO_TPM = lib.TSS2_FAPI_RC_NO_TPM
    FAPI_RC_TRY_AGAIN = lib.TSS2_FAPI_RC_TRY_AGAIN
    FAPI_RC_BAD_KEY = lib.TSS2_FAPI_RC_BAD_KEY
    FAPI_RC_NO_HANDLE = lib.TSS2_FAPI_RC_NO_HANDLE
    FAPI_RC_NOT_PROVISIONED = lib.TSS2_FAPI_RC_NOT_PROVISIONED
    FAPI_RC_ALREADY_PROVISIONED = lib.TSS2_FAPI_RC_ALREADY_PROVISIONED

    def __init__(self, rc):
        errmsg = ffi.string(lib.Tss2_RC_Decode(rc)).decode()
        super(TSS2_Exception, self).__init__(f"{errmsg}")

        self.rc = rc
        self.handle = 0
        self.parameter = 0
        self.session = 0
        self.error = 0
        if self.rc & lib.TPM2_RC_FMT1:
            self._parse_fmt1()
        else:
            self.error = self.rc

    def _parse_fmt1(self):
        self.error = lib.TPM2_RC_FMT1 + (self.rc & 0x3F)

        if self.rc & lib.TPM2_RC_P:
            self.parameter = (self.rc & lib.TPM2_RC_N_MASK) >> 8
        elif self.rc & lib.TPM2_RC_S:
            self.session = ((self.rc - lib.TPM2_RC_S) & lib.TPM2_RC_N_MASK) >> 8
        else:
            self.handle = (self.rc & lib.TPM2_RC_N_MASK) >> 8
