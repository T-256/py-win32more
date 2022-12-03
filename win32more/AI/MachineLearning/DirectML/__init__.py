from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.AI.MachineLearning.DirectML
import win32more.Foundation
import win32more.Graphics.Direct3D12
import win32more.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
DML_TARGET_VERSION = 16384
DML_TENSOR_DIMENSION_COUNT_MAX = 5
DML_TENSOR_DIMENSION_COUNT_MAX1 = 8
DML_TEMPORARY_BUFFER_ALIGNMENT = 256
DML_PERSISTENT_BUFFER_ALIGNMENT = 256
DML_MINIMUM_BUFFER_TENSOR_ALIGNMENT = 16
def _define_DMLCreateDevice():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Device_head,win32more.AI.MachineLearning.DirectML.DML_CREATE_DEVICE_FLAGS,POINTER(Guid),POINTER(c_void_p))(('DMLCreateDevice', windll['DirectML.dll']), ((1, 'd3d12Device'),(1, 'flags'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DMLCreateDevice1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Device_head,win32more.AI.MachineLearning.DirectML.DML_CREATE_DEVICE_FLAGS,win32more.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL,POINTER(Guid),POINTER(c_void_p))(('DMLCreateDevice1', windll['DirectML.dll']), ((1, 'd3d12Device'),(1, 'flags'),(1, 'minimumFeatureLevel'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DML_ACTIVATION_CELU_OPERATOR_DESC_head():
    class DML_ACTIVATION_CELU_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_CELU_OPERATOR_DESC
def _define_DML_ACTIVATION_CELU_OPERATOR_DESC():
    DML_ACTIVATION_CELU_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_CELU_OPERATOR_DESC_head
    DML_ACTIVATION_CELU_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Alpha', Single),
    ]
    return DML_ACTIVATION_CELU_OPERATOR_DESC
def _define_DML_ACTIVATION_ELU_OPERATOR_DESC_head():
    class DML_ACTIVATION_ELU_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_ELU_OPERATOR_DESC
def _define_DML_ACTIVATION_ELU_OPERATOR_DESC():
    DML_ACTIVATION_ELU_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_ELU_OPERATOR_DESC_head
    DML_ACTIVATION_ELU_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Alpha', Single),
    ]
    return DML_ACTIVATION_ELU_OPERATOR_DESC
def _define_DML_ACTIVATION_HARD_SIGMOID_OPERATOR_DESC_head():
    class DML_ACTIVATION_HARD_SIGMOID_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_HARD_SIGMOID_OPERATOR_DESC
def _define_DML_ACTIVATION_HARD_SIGMOID_OPERATOR_DESC():
    DML_ACTIVATION_HARD_SIGMOID_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_HARD_SIGMOID_OPERATOR_DESC_head
    DML_ACTIVATION_HARD_SIGMOID_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Alpha', Single),
        ('Beta', Single),
    ]
    return DML_ACTIVATION_HARD_SIGMOID_OPERATOR_DESC
def _define_DML_ACTIVATION_HARDMAX_OPERATOR_DESC_head():
    class DML_ACTIVATION_HARDMAX_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_HARDMAX_OPERATOR_DESC
def _define_DML_ACTIVATION_HARDMAX_OPERATOR_DESC():
    DML_ACTIVATION_HARDMAX_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_HARDMAX_OPERATOR_DESC_head
    DML_ACTIVATION_HARDMAX_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ACTIVATION_HARDMAX_OPERATOR_DESC
def _define_DML_ACTIVATION_IDENTITY_OPERATOR_DESC_head():
    class DML_ACTIVATION_IDENTITY_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_IDENTITY_OPERATOR_DESC
def _define_DML_ACTIVATION_IDENTITY_OPERATOR_DESC():
    DML_ACTIVATION_IDENTITY_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_IDENTITY_OPERATOR_DESC_head
    DML_ACTIVATION_IDENTITY_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ACTIVATION_IDENTITY_OPERATOR_DESC
def _define_DML_ACTIVATION_LEAKY_RELU_OPERATOR_DESC_head():
    class DML_ACTIVATION_LEAKY_RELU_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_LEAKY_RELU_OPERATOR_DESC
def _define_DML_ACTIVATION_LEAKY_RELU_OPERATOR_DESC():
    DML_ACTIVATION_LEAKY_RELU_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_LEAKY_RELU_OPERATOR_DESC_head
    DML_ACTIVATION_LEAKY_RELU_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Alpha', Single),
    ]
    return DML_ACTIVATION_LEAKY_RELU_OPERATOR_DESC
def _define_DML_ACTIVATION_LINEAR_OPERATOR_DESC_head():
    class DML_ACTIVATION_LINEAR_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_LINEAR_OPERATOR_DESC
def _define_DML_ACTIVATION_LINEAR_OPERATOR_DESC():
    DML_ACTIVATION_LINEAR_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_LINEAR_OPERATOR_DESC_head
    DML_ACTIVATION_LINEAR_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Alpha', Single),
        ('Beta', Single),
    ]
    return DML_ACTIVATION_LINEAR_OPERATOR_DESC
def _define_DML_ACTIVATION_LOG_SOFTMAX_OPERATOR_DESC_head():
    class DML_ACTIVATION_LOG_SOFTMAX_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_LOG_SOFTMAX_OPERATOR_DESC
def _define_DML_ACTIVATION_LOG_SOFTMAX_OPERATOR_DESC():
    DML_ACTIVATION_LOG_SOFTMAX_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_LOG_SOFTMAX_OPERATOR_DESC_head
    DML_ACTIVATION_LOG_SOFTMAX_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ACTIVATION_LOG_SOFTMAX_OPERATOR_DESC
def _define_DML_ACTIVATION_PARAMETERIZED_RELU_OPERATOR_DESC_head():
    class DML_ACTIVATION_PARAMETERIZED_RELU_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_PARAMETERIZED_RELU_OPERATOR_DESC
def _define_DML_ACTIVATION_PARAMETERIZED_RELU_OPERATOR_DESC():
    DML_ACTIVATION_PARAMETERIZED_RELU_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_PARAMETERIZED_RELU_OPERATOR_DESC_head
    DML_ACTIVATION_PARAMETERIZED_RELU_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('SlopeTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ACTIVATION_PARAMETERIZED_RELU_OPERATOR_DESC
def _define_DML_ACTIVATION_PARAMETRIC_SOFTPLUS_OPERATOR_DESC_head():
    class DML_ACTIVATION_PARAMETRIC_SOFTPLUS_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_PARAMETRIC_SOFTPLUS_OPERATOR_DESC
def _define_DML_ACTIVATION_PARAMETRIC_SOFTPLUS_OPERATOR_DESC():
    DML_ACTIVATION_PARAMETRIC_SOFTPLUS_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_PARAMETRIC_SOFTPLUS_OPERATOR_DESC_head
    DML_ACTIVATION_PARAMETRIC_SOFTPLUS_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Alpha', Single),
        ('Beta', Single),
    ]
    return DML_ACTIVATION_PARAMETRIC_SOFTPLUS_OPERATOR_DESC
def _define_DML_ACTIVATION_RELU_GRAD_OPERATOR_DESC_head():
    class DML_ACTIVATION_RELU_GRAD_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_RELU_GRAD_OPERATOR_DESC
def _define_DML_ACTIVATION_RELU_GRAD_OPERATOR_DESC():
    DML_ACTIVATION_RELU_GRAD_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_RELU_GRAD_OPERATOR_DESC_head
    DML_ACTIVATION_RELU_GRAD_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InputGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ACTIVATION_RELU_GRAD_OPERATOR_DESC
def _define_DML_ACTIVATION_RELU_OPERATOR_DESC_head():
    class DML_ACTIVATION_RELU_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_RELU_OPERATOR_DESC
def _define_DML_ACTIVATION_RELU_OPERATOR_DESC():
    DML_ACTIVATION_RELU_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_RELU_OPERATOR_DESC_head
    DML_ACTIVATION_RELU_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ACTIVATION_RELU_OPERATOR_DESC
def _define_DML_ACTIVATION_SCALED_ELU_OPERATOR_DESC_head():
    class DML_ACTIVATION_SCALED_ELU_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_SCALED_ELU_OPERATOR_DESC
def _define_DML_ACTIVATION_SCALED_ELU_OPERATOR_DESC():
    DML_ACTIVATION_SCALED_ELU_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_SCALED_ELU_OPERATOR_DESC_head
    DML_ACTIVATION_SCALED_ELU_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Alpha', Single),
        ('Gamma', Single),
    ]
    return DML_ACTIVATION_SCALED_ELU_OPERATOR_DESC
def _define_DML_ACTIVATION_SCALED_TANH_OPERATOR_DESC_head():
    class DML_ACTIVATION_SCALED_TANH_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_SCALED_TANH_OPERATOR_DESC
def _define_DML_ACTIVATION_SCALED_TANH_OPERATOR_DESC():
    DML_ACTIVATION_SCALED_TANH_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_SCALED_TANH_OPERATOR_DESC_head
    DML_ACTIVATION_SCALED_TANH_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Alpha', Single),
        ('Beta', Single),
    ]
    return DML_ACTIVATION_SCALED_TANH_OPERATOR_DESC
def _define_DML_ACTIVATION_SHRINK_OPERATOR_DESC_head():
    class DML_ACTIVATION_SHRINK_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_SHRINK_OPERATOR_DESC
def _define_DML_ACTIVATION_SHRINK_OPERATOR_DESC():
    DML_ACTIVATION_SHRINK_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_SHRINK_OPERATOR_DESC_head
    DML_ACTIVATION_SHRINK_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Bias', Single),
        ('Threshold', Single),
    ]
    return DML_ACTIVATION_SHRINK_OPERATOR_DESC
def _define_DML_ACTIVATION_SIGMOID_OPERATOR_DESC_head():
    class DML_ACTIVATION_SIGMOID_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_SIGMOID_OPERATOR_DESC
def _define_DML_ACTIVATION_SIGMOID_OPERATOR_DESC():
    DML_ACTIVATION_SIGMOID_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_SIGMOID_OPERATOR_DESC_head
    DML_ACTIVATION_SIGMOID_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ACTIVATION_SIGMOID_OPERATOR_DESC
def _define_DML_ACTIVATION_SOFTMAX_OPERATOR_DESC_head():
    class DML_ACTIVATION_SOFTMAX_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_SOFTMAX_OPERATOR_DESC
def _define_DML_ACTIVATION_SOFTMAX_OPERATOR_DESC():
    DML_ACTIVATION_SOFTMAX_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_SOFTMAX_OPERATOR_DESC_head
    DML_ACTIVATION_SOFTMAX_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ACTIVATION_SOFTMAX_OPERATOR_DESC
def _define_DML_ACTIVATION_SOFTPLUS_OPERATOR_DESC_head():
    class DML_ACTIVATION_SOFTPLUS_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_SOFTPLUS_OPERATOR_DESC
def _define_DML_ACTIVATION_SOFTPLUS_OPERATOR_DESC():
    DML_ACTIVATION_SOFTPLUS_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_SOFTPLUS_OPERATOR_DESC_head
    DML_ACTIVATION_SOFTPLUS_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Steepness', Single),
    ]
    return DML_ACTIVATION_SOFTPLUS_OPERATOR_DESC
def _define_DML_ACTIVATION_SOFTSIGN_OPERATOR_DESC_head():
    class DML_ACTIVATION_SOFTSIGN_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_SOFTSIGN_OPERATOR_DESC
def _define_DML_ACTIVATION_SOFTSIGN_OPERATOR_DESC():
    DML_ACTIVATION_SOFTSIGN_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_SOFTSIGN_OPERATOR_DESC_head
    DML_ACTIVATION_SOFTSIGN_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ACTIVATION_SOFTSIGN_OPERATOR_DESC
def _define_DML_ACTIVATION_TANH_OPERATOR_DESC_head():
    class DML_ACTIVATION_TANH_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_TANH_OPERATOR_DESC
def _define_DML_ACTIVATION_TANH_OPERATOR_DESC():
    DML_ACTIVATION_TANH_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_TANH_OPERATOR_DESC_head
    DML_ACTIVATION_TANH_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ACTIVATION_TANH_OPERATOR_DESC
def _define_DML_ACTIVATION_THRESHOLDED_RELU_OPERATOR_DESC_head():
    class DML_ACTIVATION_THRESHOLDED_RELU_OPERATOR_DESC(Structure):
        pass
    return DML_ACTIVATION_THRESHOLDED_RELU_OPERATOR_DESC
def _define_DML_ACTIVATION_THRESHOLDED_RELU_OPERATOR_DESC():
    DML_ACTIVATION_THRESHOLDED_RELU_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ACTIVATION_THRESHOLDED_RELU_OPERATOR_DESC_head
    DML_ACTIVATION_THRESHOLDED_RELU_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Alpha', Single),
    ]
    return DML_ACTIVATION_THRESHOLDED_RELU_OPERATOR_DESC
def _define_DML_ADAM_OPTIMIZER_OPERATOR_DESC_head():
    class DML_ADAM_OPTIMIZER_OPERATOR_DESC(Structure):
        pass
    return DML_ADAM_OPTIMIZER_OPERATOR_DESC
def _define_DML_ADAM_OPTIMIZER_OPERATOR_DESC():
    DML_ADAM_OPTIMIZER_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ADAM_OPTIMIZER_OPERATOR_DESC_head
    DML_ADAM_OPTIMIZER_OPERATOR_DESC._fields_ = [
        ('InputParametersTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InputFirstMomentTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InputSecondMomentTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('GradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('TrainingStepTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputParametersTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputFirstMomentTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputSecondMomentTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('LearningRate', Single),
        ('Beta1', Single),
        ('Beta2', Single),
        ('Epsilon', Single),
    ]
    return DML_ADAM_OPTIMIZER_OPERATOR_DESC
def _define_DML_ARGMAX_OPERATOR_DESC_head():
    class DML_ARGMAX_OPERATOR_DESC(Structure):
        pass
    return DML_ARGMAX_OPERATOR_DESC
def _define_DML_ARGMAX_OPERATOR_DESC():
    DML_ARGMAX_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ARGMAX_OPERATOR_DESC_head
    DML_ARGMAX_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('AxisCount', UInt32),
        ('Axes', POINTER(UInt32)),
        ('AxisDirection', win32more.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION),
    ]
    return DML_ARGMAX_OPERATOR_DESC
def _define_DML_ARGMIN_OPERATOR_DESC_head():
    class DML_ARGMIN_OPERATOR_DESC(Structure):
        pass
    return DML_ARGMIN_OPERATOR_DESC
def _define_DML_ARGMIN_OPERATOR_DESC():
    DML_ARGMIN_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ARGMIN_OPERATOR_DESC_head
    DML_ARGMIN_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('AxisCount', UInt32),
        ('Axes', POINTER(UInt32)),
        ('AxisDirection', win32more.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION),
    ]
    return DML_ARGMIN_OPERATOR_DESC
def _define_DML_AVERAGE_POOLING_GRAD_OPERATOR_DESC_head():
    class DML_AVERAGE_POOLING_GRAD_OPERATOR_DESC(Structure):
        pass
    return DML_AVERAGE_POOLING_GRAD_OPERATOR_DESC
def _define_DML_AVERAGE_POOLING_GRAD_OPERATOR_DESC():
    DML_AVERAGE_POOLING_GRAD_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_AVERAGE_POOLING_GRAD_OPERATOR_DESC_head
    DML_AVERAGE_POOLING_GRAD_OPERATOR_DESC._fields_ = [
        ('InputGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('DimensionCount', UInt32),
        ('Strides', POINTER(UInt32)),
        ('WindowSize', POINTER(UInt32)),
        ('StartPadding', POINTER(UInt32)),
        ('EndPadding', POINTER(UInt32)),
        ('IncludePadding', win32more.Foundation.BOOL),
    ]
    return DML_AVERAGE_POOLING_GRAD_OPERATOR_DESC
def _define_DML_AVERAGE_POOLING_OPERATOR_DESC_head():
    class DML_AVERAGE_POOLING_OPERATOR_DESC(Structure):
        pass
    return DML_AVERAGE_POOLING_OPERATOR_DESC
def _define_DML_AVERAGE_POOLING_OPERATOR_DESC():
    DML_AVERAGE_POOLING_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_AVERAGE_POOLING_OPERATOR_DESC_head
    DML_AVERAGE_POOLING_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('DimensionCount', UInt32),
        ('Strides', POINTER(UInt32)),
        ('WindowSize', POINTER(UInt32)),
        ('StartPadding', POINTER(UInt32)),
        ('EndPadding', POINTER(UInt32)),
        ('IncludePadding', win32more.Foundation.BOOL),
    ]
    return DML_AVERAGE_POOLING_OPERATOR_DESC
DML_AXIS_DIRECTION = Int32
DML_AXIS_DIRECTION_INCREASING = 0
DML_AXIS_DIRECTION_DECREASING = 1
def _define_DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC_head():
    class DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC(Structure):
        pass
    return DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC
def _define_DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC():
    DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC_head
    DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InputGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('MeanTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('VarianceTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputScaleGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputBiasGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Epsilon', Single),
    ]
    return DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC
def _define_DML_BATCH_NORMALIZATION_OPERATOR_DESC_head():
    class DML_BATCH_NORMALIZATION_OPERATOR_DESC(Structure):
        pass
    return DML_BATCH_NORMALIZATION_OPERATOR_DESC
def _define_DML_BATCH_NORMALIZATION_OPERATOR_DESC():
    DML_BATCH_NORMALIZATION_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_BATCH_NORMALIZATION_OPERATOR_DESC_head
    DML_BATCH_NORMALIZATION_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('MeanTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('VarianceTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BiasTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Spatial', win32more.Foundation.BOOL),
        ('Epsilon', Single),
        ('FusedActivation', POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)),
    ]
    return DML_BATCH_NORMALIZATION_OPERATOR_DESC
def _define_DML_BINDING_DESC_head():
    class DML_BINDING_DESC(Structure):
        pass
    return DML_BINDING_DESC
def _define_DML_BINDING_DESC():
    DML_BINDING_DESC = win32more.AI.MachineLearning.DirectML.DML_BINDING_DESC_head
    DML_BINDING_DESC._fields_ = [
        ('Type', win32more.AI.MachineLearning.DirectML.DML_BINDING_TYPE),
        ('Desc', c_void_p),
    ]
    return DML_BINDING_DESC
def _define_DML_BINDING_PROPERTIES_head():
    class DML_BINDING_PROPERTIES(Structure):
        pass
    return DML_BINDING_PROPERTIES
def _define_DML_BINDING_PROPERTIES():
    DML_BINDING_PROPERTIES = win32more.AI.MachineLearning.DirectML.DML_BINDING_PROPERTIES_head
    DML_BINDING_PROPERTIES._fields_ = [
        ('RequiredDescriptorCount', UInt32),
        ('TemporaryResourceSize', UInt64),
        ('PersistentResourceSize', UInt64),
    ]
    return DML_BINDING_PROPERTIES
def _define_DML_BINDING_TABLE_DESC_head():
    class DML_BINDING_TABLE_DESC(Structure):
        pass
    return DML_BINDING_TABLE_DESC
def _define_DML_BINDING_TABLE_DESC():
    DML_BINDING_TABLE_DESC = win32more.AI.MachineLearning.DirectML.DML_BINDING_TABLE_DESC_head
    DML_BINDING_TABLE_DESC._fields_ = [
        ('Dispatchable', win32more.AI.MachineLearning.DirectML.IDMLDispatchable_head),
        ('CPUDescriptorHandle', win32more.Graphics.Direct3D12.D3D12_CPU_DESCRIPTOR_HANDLE),
        ('GPUDescriptorHandle', win32more.Graphics.Direct3D12.D3D12_GPU_DESCRIPTOR_HANDLE),
        ('SizeInDescriptors', UInt32),
    ]
    return DML_BINDING_TABLE_DESC
DML_BINDING_TYPE = Int32
DML_BINDING_TYPE_NONE = 0
DML_BINDING_TYPE_BUFFER = 1
DML_BINDING_TYPE_BUFFER_ARRAY = 2
def _define_DML_BUFFER_ARRAY_BINDING_head():
    class DML_BUFFER_ARRAY_BINDING(Structure):
        pass
    return DML_BUFFER_ARRAY_BINDING
def _define_DML_BUFFER_ARRAY_BINDING():
    DML_BUFFER_ARRAY_BINDING = win32more.AI.MachineLearning.DirectML.DML_BUFFER_ARRAY_BINDING_head
    DML_BUFFER_ARRAY_BINDING._fields_ = [
        ('BindingCount', UInt32),
        ('Bindings', POINTER(win32more.AI.MachineLearning.DirectML.DML_BUFFER_BINDING_head)),
    ]
    return DML_BUFFER_ARRAY_BINDING
def _define_DML_BUFFER_BINDING_head():
    class DML_BUFFER_BINDING(Structure):
        pass
    return DML_BUFFER_BINDING
def _define_DML_BUFFER_BINDING():
    DML_BUFFER_BINDING = win32more.AI.MachineLearning.DirectML.DML_BUFFER_BINDING_head
    DML_BUFFER_BINDING._fields_ = [
        ('Buffer', win32more.Graphics.Direct3D12.ID3D12Resource_head),
        ('Offset', UInt64),
        ('SizeInBytes', UInt64),
    ]
    return DML_BUFFER_BINDING
def _define_DML_BUFFER_TENSOR_DESC_head():
    class DML_BUFFER_TENSOR_DESC(Structure):
        pass
    return DML_BUFFER_TENSOR_DESC
def _define_DML_BUFFER_TENSOR_DESC():
    DML_BUFFER_TENSOR_DESC = win32more.AI.MachineLearning.DirectML.DML_BUFFER_TENSOR_DESC_head
    DML_BUFFER_TENSOR_DESC._fields_ = [
        ('DataType', win32more.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE),
        ('Flags', win32more.AI.MachineLearning.DirectML.DML_TENSOR_FLAGS),
        ('DimensionCount', UInt32),
        ('Sizes', POINTER(UInt32)),
        ('Strides', POINTER(UInt32)),
        ('TotalTensorSizeInBytes', UInt64),
        ('GuaranteedBaseOffsetAlignment', UInt32),
    ]
    return DML_BUFFER_TENSOR_DESC
def _define_DML_CAST_OPERATOR_DESC_head():
    class DML_CAST_OPERATOR_DESC(Structure):
        pass
    return DML_CAST_OPERATOR_DESC
def _define_DML_CAST_OPERATOR_DESC():
    DML_CAST_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_CAST_OPERATOR_DESC_head
    DML_CAST_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_CAST_OPERATOR_DESC
DML_CONVOLUTION_DIRECTION = Int32
DML_CONVOLUTION_DIRECTION_FORWARD = 0
DML_CONVOLUTION_DIRECTION_BACKWARD = 1
def _define_DML_CONVOLUTION_INTEGER_OPERATOR_DESC_head():
    class DML_CONVOLUTION_INTEGER_OPERATOR_DESC(Structure):
        pass
    return DML_CONVOLUTION_INTEGER_OPERATOR_DESC
def _define_DML_CONVOLUTION_INTEGER_OPERATOR_DESC():
    DML_CONVOLUTION_INTEGER_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_CONVOLUTION_INTEGER_OPERATOR_DESC_head
    DML_CONVOLUTION_INTEGER_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InputZeroPointTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('FilterTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('FilterZeroPointTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('DimensionCount', UInt32),
        ('Strides', POINTER(UInt32)),
        ('Dilations', POINTER(UInt32)),
        ('StartPadding', POINTER(UInt32)),
        ('EndPadding', POINTER(UInt32)),
        ('GroupCount', UInt32),
    ]
    return DML_CONVOLUTION_INTEGER_OPERATOR_DESC
DML_CONVOLUTION_MODE = Int32
DML_CONVOLUTION_MODE_CONVOLUTION = 0
DML_CONVOLUTION_MODE_CROSS_CORRELATION = 1
def _define_DML_CONVOLUTION_OPERATOR_DESC_head():
    class DML_CONVOLUTION_OPERATOR_DESC(Structure):
        pass
    return DML_CONVOLUTION_OPERATOR_DESC
def _define_DML_CONVOLUTION_OPERATOR_DESC():
    DML_CONVOLUTION_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_CONVOLUTION_OPERATOR_DESC_head
    DML_CONVOLUTION_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('FilterTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BiasTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Mode', win32more.AI.MachineLearning.DirectML.DML_CONVOLUTION_MODE),
        ('Direction', win32more.AI.MachineLearning.DirectML.DML_CONVOLUTION_DIRECTION),
        ('DimensionCount', UInt32),
        ('Strides', POINTER(UInt32)),
        ('Dilations', POINTER(UInt32)),
        ('StartPadding', POINTER(UInt32)),
        ('EndPadding', POINTER(UInt32)),
        ('OutputPadding', POINTER(UInt32)),
        ('GroupCount', UInt32),
        ('FusedActivation', POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)),
    ]
    return DML_CONVOLUTION_OPERATOR_DESC
DML_CREATE_DEVICE_FLAGS = UInt32
DML_CREATE_DEVICE_FLAG_NONE = 0
DML_CREATE_DEVICE_FLAG_DEBUG = 1
def _define_DML_CUMULATIVE_PRODUCT_OPERATOR_DESC_head():
    class DML_CUMULATIVE_PRODUCT_OPERATOR_DESC(Structure):
        pass
    return DML_CUMULATIVE_PRODUCT_OPERATOR_DESC
def _define_DML_CUMULATIVE_PRODUCT_OPERATOR_DESC():
    DML_CUMULATIVE_PRODUCT_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_CUMULATIVE_PRODUCT_OPERATOR_DESC_head
    DML_CUMULATIVE_PRODUCT_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Axis', UInt32),
        ('AxisDirection', win32more.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION),
        ('HasExclusiveProduct', win32more.Foundation.BOOL),
    ]
    return DML_CUMULATIVE_PRODUCT_OPERATOR_DESC
def _define_DML_CUMULATIVE_SUMMATION_OPERATOR_DESC_head():
    class DML_CUMULATIVE_SUMMATION_OPERATOR_DESC(Structure):
        pass
    return DML_CUMULATIVE_SUMMATION_OPERATOR_DESC
def _define_DML_CUMULATIVE_SUMMATION_OPERATOR_DESC():
    DML_CUMULATIVE_SUMMATION_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_CUMULATIVE_SUMMATION_OPERATOR_DESC_head
    DML_CUMULATIVE_SUMMATION_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Axis', UInt32),
        ('AxisDirection', win32more.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION),
        ('HasExclusiveSum', win32more.Foundation.BOOL),
    ]
    return DML_CUMULATIVE_SUMMATION_OPERATOR_DESC
DML_DEPTH_SPACE_ORDER = Int32
DML_DEPTH_SPACE_ORDER_DEPTH_COLUMN_ROW = 0
DML_DEPTH_SPACE_ORDER_COLUMN_ROW_DEPTH = 1
def _define_DML_DEPTH_TO_SPACE_OPERATOR_DESC_head():
    class DML_DEPTH_TO_SPACE_OPERATOR_DESC(Structure):
        pass
    return DML_DEPTH_TO_SPACE_OPERATOR_DESC
def _define_DML_DEPTH_TO_SPACE_OPERATOR_DESC():
    DML_DEPTH_TO_SPACE_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_DEPTH_TO_SPACE_OPERATOR_DESC_head
    DML_DEPTH_TO_SPACE_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BlockSize', UInt32),
    ]
    return DML_DEPTH_TO_SPACE_OPERATOR_DESC
def _define_DML_DEPTH_TO_SPACE1_OPERATOR_DESC_head():
    class DML_DEPTH_TO_SPACE1_OPERATOR_DESC(Structure):
        pass
    return DML_DEPTH_TO_SPACE1_OPERATOR_DESC
def _define_DML_DEPTH_TO_SPACE1_OPERATOR_DESC():
    DML_DEPTH_TO_SPACE1_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_DEPTH_TO_SPACE1_OPERATOR_DESC_head
    DML_DEPTH_TO_SPACE1_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BlockSize', UInt32),
        ('Order', win32more.AI.MachineLearning.DirectML.DML_DEPTH_SPACE_ORDER),
    ]
    return DML_DEPTH_TO_SPACE1_OPERATOR_DESC
def _define_DML_DIAGONAL_MATRIX_OPERATOR_DESC_head():
    class DML_DIAGONAL_MATRIX_OPERATOR_DESC(Structure):
        pass
    return DML_DIAGONAL_MATRIX_OPERATOR_DESC
def _define_DML_DIAGONAL_MATRIX_OPERATOR_DESC():
    DML_DIAGONAL_MATRIX_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_DIAGONAL_MATRIX_OPERATOR_DESC_head
    DML_DIAGONAL_MATRIX_OPERATOR_DESC._fields_ = [
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Offset', Int32),
        ('Value', Single),
    ]
    return DML_DIAGONAL_MATRIX_OPERATOR_DESC
def _define_DML_DYNAMIC_QUANTIZE_LINEAR_OPERATOR_DESC_head():
    class DML_DYNAMIC_QUANTIZE_LINEAR_OPERATOR_DESC(Structure):
        pass
    return DML_DYNAMIC_QUANTIZE_LINEAR_OPERATOR_DESC
def _define_DML_DYNAMIC_QUANTIZE_LINEAR_OPERATOR_DESC():
    DML_DYNAMIC_QUANTIZE_LINEAR_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_DYNAMIC_QUANTIZE_LINEAR_OPERATOR_DESC_head
    DML_DYNAMIC_QUANTIZE_LINEAR_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputScaleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputZeroPointTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_DYNAMIC_QUANTIZE_LINEAR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ABS_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_ABS_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_ABS_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ABS_OPERATOR_DESC():
    DML_ELEMENT_WISE_ABS_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_ABS_OPERATOR_DESC_head
    DML_ELEMENT_WISE_ABS_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_ABS_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ACOS_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_ACOS_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_ACOS_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ACOS_OPERATOR_DESC():
    DML_ELEMENT_WISE_ACOS_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_ACOS_OPERATOR_DESC_head
    DML_ELEMENT_WISE_ACOS_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_ACOS_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ACOSH_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_ACOSH_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_ACOSH_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ACOSH_OPERATOR_DESC():
    DML_ELEMENT_WISE_ACOSH_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_ACOSH_OPERATOR_DESC_head
    DML_ELEMENT_WISE_ACOSH_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_ACOSH_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ADD_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_ADD_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_ADD_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ADD_OPERATOR_DESC():
    DML_ELEMENT_WISE_ADD_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_ADD_OPERATOR_DESC_head
    DML_ELEMENT_WISE_ADD_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_ADD_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ADD1_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_ADD1_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_ADD1_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ADD1_OPERATOR_DESC():
    DML_ELEMENT_WISE_ADD1_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_ADD1_OPERATOR_DESC_head
    DML_ELEMENT_WISE_ADD1_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('FusedActivation', POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_ADD1_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ASIN_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_ASIN_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_ASIN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ASIN_OPERATOR_DESC():
    DML_ELEMENT_WISE_ASIN_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_ASIN_OPERATOR_DESC_head
    DML_ELEMENT_WISE_ASIN_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_ASIN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ASINH_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_ASINH_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_ASINH_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ASINH_OPERATOR_DESC():
    DML_ELEMENT_WISE_ASINH_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_ASINH_OPERATOR_DESC_head
    DML_ELEMENT_WISE_ASINH_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_ASINH_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ATAN_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_ATAN_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_ATAN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ATAN_OPERATOR_DESC():
    DML_ELEMENT_WISE_ATAN_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_ATAN_OPERATOR_DESC_head
    DML_ELEMENT_WISE_ATAN_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_ATAN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ATAN_YX_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_ATAN_YX_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_ATAN_YX_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ATAN_YX_OPERATOR_DESC():
    DML_ELEMENT_WISE_ATAN_YX_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_ATAN_YX_OPERATOR_DESC_head
    DML_ELEMENT_WISE_ATAN_YX_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_ATAN_YX_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ATANH_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_ATANH_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_ATANH_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ATANH_OPERATOR_DESC():
    DML_ELEMENT_WISE_ATANH_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_ATANH_OPERATOR_DESC_head
    DML_ELEMENT_WISE_ATANH_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_ATANH_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC():
    DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC_head
    DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_BIT_COUNT_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_BIT_COUNT_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_BIT_COUNT_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_BIT_COUNT_OPERATOR_DESC():
    DML_ELEMENT_WISE_BIT_COUNT_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_BIT_COUNT_OPERATOR_DESC_head
    DML_ELEMENT_WISE_BIT_COUNT_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_BIT_COUNT_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_BIT_NOT_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_BIT_NOT_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_BIT_NOT_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_BIT_NOT_OPERATOR_DESC():
    DML_ELEMENT_WISE_BIT_NOT_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_BIT_NOT_OPERATOR_DESC_head
    DML_ELEMENT_WISE_BIT_NOT_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_BIT_NOT_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_BIT_OR_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_BIT_OR_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_BIT_OR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_BIT_OR_OPERATOR_DESC():
    DML_ELEMENT_WISE_BIT_OR_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_BIT_OR_OPERATOR_DESC_head
    DML_ELEMENT_WISE_BIT_OR_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_BIT_OR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_BIT_SHIFT_LEFT_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_BIT_SHIFT_LEFT_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_BIT_SHIFT_LEFT_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_BIT_SHIFT_LEFT_OPERATOR_DESC():
    DML_ELEMENT_WISE_BIT_SHIFT_LEFT_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_BIT_SHIFT_LEFT_OPERATOR_DESC_head
    DML_ELEMENT_WISE_BIT_SHIFT_LEFT_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_BIT_SHIFT_LEFT_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_BIT_SHIFT_RIGHT_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_BIT_SHIFT_RIGHT_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_BIT_SHIFT_RIGHT_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_BIT_SHIFT_RIGHT_OPERATOR_DESC():
    DML_ELEMENT_WISE_BIT_SHIFT_RIGHT_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_BIT_SHIFT_RIGHT_OPERATOR_DESC_head
    DML_ELEMENT_WISE_BIT_SHIFT_RIGHT_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_BIT_SHIFT_RIGHT_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_BIT_XOR_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_BIT_XOR_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_BIT_XOR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_BIT_XOR_OPERATOR_DESC():
    DML_ELEMENT_WISE_BIT_XOR_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_BIT_XOR_OPERATOR_DESC_head
    DML_ELEMENT_WISE_BIT_XOR_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_BIT_XOR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_CEIL_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_CEIL_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_CEIL_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_CEIL_OPERATOR_DESC():
    DML_ELEMENT_WISE_CEIL_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_CEIL_OPERATOR_DESC_head
    DML_ELEMENT_WISE_CEIL_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_CEIL_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_CLIP_GRAD_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_CLIP_GRAD_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_CLIP_GRAD_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_CLIP_GRAD_OPERATOR_DESC():
    DML_ELEMENT_WISE_CLIP_GRAD_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_CLIP_GRAD_OPERATOR_DESC_head
    DML_ELEMENT_WISE_CLIP_GRAD_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InputGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Min', Single),
        ('Max', Single),
    ]
    return DML_ELEMENT_WISE_CLIP_GRAD_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_CLIP_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_CLIP_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_CLIP_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_CLIP_OPERATOR_DESC():
    DML_ELEMENT_WISE_CLIP_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_CLIP_OPERATOR_DESC_head
    DML_ELEMENT_WISE_CLIP_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
        ('Min', Single),
        ('Max', Single),
    ]
    return DML_ELEMENT_WISE_CLIP_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_CONSTANT_POW_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_CONSTANT_POW_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_CONSTANT_POW_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_CONSTANT_POW_OPERATOR_DESC():
    DML_ELEMENT_WISE_CONSTANT_POW_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_CONSTANT_POW_OPERATOR_DESC_head
    DML_ELEMENT_WISE_CONSTANT_POW_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
        ('Exponent', Single),
    ]
    return DML_ELEMENT_WISE_CONSTANT_POW_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_COS_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_COS_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_COS_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_COS_OPERATOR_DESC():
    DML_ELEMENT_WISE_COS_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_COS_OPERATOR_DESC_head
    DML_ELEMENT_WISE_COS_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_COS_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_COSH_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_COSH_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_COSH_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_COSH_OPERATOR_DESC():
    DML_ELEMENT_WISE_COSH_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_COSH_OPERATOR_DESC_head
    DML_ELEMENT_WISE_COSH_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_COSH_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_DEQUANTIZE_LINEAR_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_DEQUANTIZE_LINEAR_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_DEQUANTIZE_LINEAR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_DEQUANTIZE_LINEAR_OPERATOR_DESC():
    DML_ELEMENT_WISE_DEQUANTIZE_LINEAR_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_DEQUANTIZE_LINEAR_OPERATOR_DESC_head
    DML_ELEMENT_WISE_DEQUANTIZE_LINEAR_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ZeroPointTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_DEQUANTIZE_LINEAR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_DIFFERENCE_SQUARE_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_DIFFERENCE_SQUARE_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_DIFFERENCE_SQUARE_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_DIFFERENCE_SQUARE_OPERATOR_DESC():
    DML_ELEMENT_WISE_DIFFERENCE_SQUARE_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_DIFFERENCE_SQUARE_OPERATOR_DESC_head
    DML_ELEMENT_WISE_DIFFERENCE_SQUARE_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_DIFFERENCE_SQUARE_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_DIVIDE_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_DIVIDE_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_DIVIDE_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_DIVIDE_OPERATOR_DESC():
    DML_ELEMENT_WISE_DIVIDE_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_DIVIDE_OPERATOR_DESC_head
    DML_ELEMENT_WISE_DIVIDE_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_DIVIDE_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ERF_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_ERF_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_ERF_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ERF_OPERATOR_DESC():
    DML_ELEMENT_WISE_ERF_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_ERF_OPERATOR_DESC_head
    DML_ELEMENT_WISE_ERF_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_ERF_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_EXP_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_EXP_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_EXP_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_EXP_OPERATOR_DESC():
    DML_ELEMENT_WISE_EXP_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_EXP_OPERATOR_DESC_head
    DML_ELEMENT_WISE_EXP_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_EXP_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_FLOOR_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_FLOOR_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_FLOOR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_FLOOR_OPERATOR_DESC():
    DML_ELEMENT_WISE_FLOOR_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_FLOOR_OPERATOR_DESC_head
    DML_ELEMENT_WISE_FLOOR_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_FLOOR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_IDENTITY_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_IDENTITY_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_IDENTITY_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_IDENTITY_OPERATOR_DESC():
    DML_ELEMENT_WISE_IDENTITY_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_IDENTITY_OPERATOR_DESC_head
    DML_ELEMENT_WISE_IDENTITY_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_IDENTITY_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_IF_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_IF_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_IF_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_IF_OPERATOR_DESC():
    DML_ELEMENT_WISE_IF_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_IF_OPERATOR_DESC_head
    DML_ELEMENT_WISE_IF_OPERATOR_DESC._fields_ = [
        ('ConditionTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_IF_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_IS_INFINITY_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_IS_INFINITY_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_IS_INFINITY_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_IS_INFINITY_OPERATOR_DESC():
    DML_ELEMENT_WISE_IS_INFINITY_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_IS_INFINITY_OPERATOR_DESC_head
    DML_ELEMENT_WISE_IS_INFINITY_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InfinityMode', win32more.AI.MachineLearning.DirectML.DML_IS_INFINITY_MODE),
    ]
    return DML_ELEMENT_WISE_IS_INFINITY_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_IS_NAN_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_IS_NAN_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_IS_NAN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_IS_NAN_OPERATOR_DESC():
    DML_ELEMENT_WISE_IS_NAN_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_IS_NAN_OPERATOR_DESC_head
    DML_ELEMENT_WISE_IS_NAN_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_IS_NAN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOG_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_LOG_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_LOG_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOG_OPERATOR_DESC():
    DML_ELEMENT_WISE_LOG_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_LOG_OPERATOR_DESC_head
    DML_ELEMENT_WISE_LOG_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_LOG_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_AND_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_LOGICAL_AND_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_LOGICAL_AND_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_AND_OPERATOR_DESC():
    DML_ELEMENT_WISE_LOGICAL_AND_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_LOGICAL_AND_OPERATOR_DESC_head
    DML_ELEMENT_WISE_LOGICAL_AND_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_LOGICAL_AND_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_EQUALS_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_LOGICAL_EQUALS_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_LOGICAL_EQUALS_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_EQUALS_OPERATOR_DESC():
    DML_ELEMENT_WISE_LOGICAL_EQUALS_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_LOGICAL_EQUALS_OPERATOR_DESC_head
    DML_ELEMENT_WISE_LOGICAL_EQUALS_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_LOGICAL_EQUALS_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OPERATOR_DESC():
    DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OPERATOR_DESC_head
    DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL_OPERATOR_DESC():
    DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL_OPERATOR_DESC_head
    DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OPERATOR_DESC():
    DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OPERATOR_DESC_head
    DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL_OPERATOR_DESC():
    DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL_OPERATOR_DESC_head
    DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_NOT_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_LOGICAL_NOT_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_LOGICAL_NOT_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_NOT_OPERATOR_DESC():
    DML_ELEMENT_WISE_LOGICAL_NOT_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_LOGICAL_NOT_OPERATOR_DESC_head
    DML_ELEMENT_WISE_LOGICAL_NOT_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_LOGICAL_NOT_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_OR_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_LOGICAL_OR_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_LOGICAL_OR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_OR_OPERATOR_DESC():
    DML_ELEMENT_WISE_LOGICAL_OR_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_LOGICAL_OR_OPERATOR_DESC_head
    DML_ELEMENT_WISE_LOGICAL_OR_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_LOGICAL_OR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_XOR_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_LOGICAL_XOR_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_LOGICAL_XOR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_LOGICAL_XOR_OPERATOR_DESC():
    DML_ELEMENT_WISE_LOGICAL_XOR_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_LOGICAL_XOR_OPERATOR_DESC_head
    DML_ELEMENT_WISE_LOGICAL_XOR_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_LOGICAL_XOR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_MAX_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_MAX_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_MAX_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_MAX_OPERATOR_DESC():
    DML_ELEMENT_WISE_MAX_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_MAX_OPERATOR_DESC_head
    DML_ELEMENT_WISE_MAX_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_MAX_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_MEAN_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_MEAN_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_MEAN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_MEAN_OPERATOR_DESC():
    DML_ELEMENT_WISE_MEAN_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_MEAN_OPERATOR_DESC_head
    DML_ELEMENT_WISE_MEAN_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_MEAN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_MIN_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_MIN_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_MIN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_MIN_OPERATOR_DESC():
    DML_ELEMENT_WISE_MIN_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_MIN_OPERATOR_DESC_head
    DML_ELEMENT_WISE_MIN_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_MIN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_MODULUS_FLOOR_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_MODULUS_FLOOR_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_MODULUS_FLOOR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_MODULUS_FLOOR_OPERATOR_DESC():
    DML_ELEMENT_WISE_MODULUS_FLOOR_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_MODULUS_FLOOR_OPERATOR_DESC_head
    DML_ELEMENT_WISE_MODULUS_FLOOR_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_MODULUS_FLOOR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_MODULUS_TRUNCATE_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_MODULUS_TRUNCATE_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_MODULUS_TRUNCATE_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_MODULUS_TRUNCATE_OPERATOR_DESC():
    DML_ELEMENT_WISE_MODULUS_TRUNCATE_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_MODULUS_TRUNCATE_OPERATOR_DESC_head
    DML_ELEMENT_WISE_MODULUS_TRUNCATE_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_MODULUS_TRUNCATE_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_MULTIPLY_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_MULTIPLY_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_MULTIPLY_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_MULTIPLY_OPERATOR_DESC():
    DML_ELEMENT_WISE_MULTIPLY_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_MULTIPLY_OPERATOR_DESC_head
    DML_ELEMENT_WISE_MULTIPLY_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_MULTIPLY_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_POW_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_POW_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_POW_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_POW_OPERATOR_DESC():
    DML_ELEMENT_WISE_POW_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_POW_OPERATOR_DESC_head
    DML_ELEMENT_WISE_POW_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ExponentTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_POW_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_QUANTIZE_LINEAR_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_QUANTIZE_LINEAR_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_QUANTIZE_LINEAR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_QUANTIZE_LINEAR_OPERATOR_DESC():
    DML_ELEMENT_WISE_QUANTIZE_LINEAR_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_QUANTIZE_LINEAR_OPERATOR_DESC_head
    DML_ELEMENT_WISE_QUANTIZE_LINEAR_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ZeroPointTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_QUANTIZE_LINEAR_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_QUANTIZED_LINEAR_ADD_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_QUANTIZED_LINEAR_ADD_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_QUANTIZED_LINEAR_ADD_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_QUANTIZED_LINEAR_ADD_OPERATOR_DESC():
    DML_ELEMENT_WISE_QUANTIZED_LINEAR_ADD_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_QUANTIZED_LINEAR_ADD_OPERATOR_DESC_head
    DML_ELEMENT_WISE_QUANTIZED_LINEAR_ADD_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('AScaleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('AZeroPointTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BScaleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BZeroPointTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputScaleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputZeroPointTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_QUANTIZED_LINEAR_ADD_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_RECIP_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_RECIP_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_RECIP_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_RECIP_OPERATOR_DESC():
    DML_ELEMENT_WISE_RECIP_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_RECIP_OPERATOR_DESC_head
    DML_ELEMENT_WISE_RECIP_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_RECIP_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ROUND_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_ROUND_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_ROUND_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_ROUND_OPERATOR_DESC():
    DML_ELEMENT_WISE_ROUND_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_ROUND_OPERATOR_DESC_head
    DML_ELEMENT_WISE_ROUND_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('RoundingMode', win32more.AI.MachineLearning.DirectML.DML_ROUNDING_MODE),
    ]
    return DML_ELEMENT_WISE_ROUND_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_SIGN_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_SIGN_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_SIGN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_SIGN_OPERATOR_DESC():
    DML_ELEMENT_WISE_SIGN_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_SIGN_OPERATOR_DESC_head
    DML_ELEMENT_WISE_SIGN_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_SIGN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_SIN_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_SIN_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_SIN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_SIN_OPERATOR_DESC():
    DML_ELEMENT_WISE_SIN_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_SIN_OPERATOR_DESC_head
    DML_ELEMENT_WISE_SIN_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_SIN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_SINH_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_SINH_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_SINH_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_SINH_OPERATOR_DESC():
    DML_ELEMENT_WISE_SINH_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_SINH_OPERATOR_DESC_head
    DML_ELEMENT_WISE_SINH_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_SINH_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_SQRT_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_SQRT_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_SQRT_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_SQRT_OPERATOR_DESC():
    DML_ELEMENT_WISE_SQRT_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_SQRT_OPERATOR_DESC_head
    DML_ELEMENT_WISE_SQRT_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_SQRT_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_SUBTRACT_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_SUBTRACT_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_SUBTRACT_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_SUBTRACT_OPERATOR_DESC():
    DML_ELEMENT_WISE_SUBTRACT_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_SUBTRACT_OPERATOR_DESC_head
    DML_ELEMENT_WISE_SUBTRACT_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_ELEMENT_WISE_SUBTRACT_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_TAN_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_TAN_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_TAN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_TAN_OPERATOR_DESC():
    DML_ELEMENT_WISE_TAN_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_TAN_OPERATOR_DESC_head
    DML_ELEMENT_WISE_TAN_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_TAN_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_TANH_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_TANH_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_TANH_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_TANH_OPERATOR_DESC():
    DML_ELEMENT_WISE_TANH_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_TANH_OPERATOR_DESC_head
    DML_ELEMENT_WISE_TANH_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
    ]
    return DML_ELEMENT_WISE_TANH_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_THRESHOLD_OPERATOR_DESC_head():
    class DML_ELEMENT_WISE_THRESHOLD_OPERATOR_DESC(Structure):
        pass
    return DML_ELEMENT_WISE_THRESHOLD_OPERATOR_DESC
def _define_DML_ELEMENT_WISE_THRESHOLD_OPERATOR_DESC():
    DML_ELEMENT_WISE_THRESHOLD_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ELEMENT_WISE_THRESHOLD_OPERATOR_DESC_head
    DML_ELEMENT_WISE_THRESHOLD_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleBias', POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)),
        ('Min', Single),
    ]
    return DML_ELEMENT_WISE_THRESHOLD_OPERATOR_DESC
DML_EXECUTION_FLAGS = UInt32
DML_EXECUTION_FLAG_NONE = 0
DML_EXECUTION_FLAG_ALLOW_HALF_PRECISION_COMPUTATION = 1
DML_EXECUTION_FLAG_DISABLE_META_COMMANDS = 2
DML_EXECUTION_FLAG_DESCRIPTORS_VOLATILE = 4
DML_FEATURE = Int32
DML_FEATURE_TENSOR_DATA_TYPE_SUPPORT = 0
DML_FEATURE_FEATURE_LEVELS = 1
def _define_DML_FEATURE_DATA_FEATURE_LEVELS_head():
    class DML_FEATURE_DATA_FEATURE_LEVELS(Structure):
        pass
    return DML_FEATURE_DATA_FEATURE_LEVELS
def _define_DML_FEATURE_DATA_FEATURE_LEVELS():
    DML_FEATURE_DATA_FEATURE_LEVELS = win32more.AI.MachineLearning.DirectML.DML_FEATURE_DATA_FEATURE_LEVELS_head
    DML_FEATURE_DATA_FEATURE_LEVELS._fields_ = [
        ('MaxSupportedFeatureLevel', win32more.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL),
    ]
    return DML_FEATURE_DATA_FEATURE_LEVELS
def _define_DML_FEATURE_DATA_TENSOR_DATA_TYPE_SUPPORT_head():
    class DML_FEATURE_DATA_TENSOR_DATA_TYPE_SUPPORT(Structure):
        pass
    return DML_FEATURE_DATA_TENSOR_DATA_TYPE_SUPPORT
def _define_DML_FEATURE_DATA_TENSOR_DATA_TYPE_SUPPORT():
    DML_FEATURE_DATA_TENSOR_DATA_TYPE_SUPPORT = win32more.AI.MachineLearning.DirectML.DML_FEATURE_DATA_TENSOR_DATA_TYPE_SUPPORT_head
    DML_FEATURE_DATA_TENSOR_DATA_TYPE_SUPPORT._fields_ = [
        ('IsSupported', win32more.Foundation.BOOL),
    ]
    return DML_FEATURE_DATA_TENSOR_DATA_TYPE_SUPPORT
DML_FEATURE_LEVEL = Int32
DML_FEATURE_LEVEL_1_0 = 4096
DML_FEATURE_LEVEL_2_0 = 8192
DML_FEATURE_LEVEL_2_1 = 8448
DML_FEATURE_LEVEL_3_0 = 12288
DML_FEATURE_LEVEL_3_1 = 12544
DML_FEATURE_LEVEL_4_0 = 16384
def _define_DML_FEATURE_QUERY_FEATURE_LEVELS_head():
    class DML_FEATURE_QUERY_FEATURE_LEVELS(Structure):
        pass
    return DML_FEATURE_QUERY_FEATURE_LEVELS
def _define_DML_FEATURE_QUERY_FEATURE_LEVELS():
    DML_FEATURE_QUERY_FEATURE_LEVELS = win32more.AI.MachineLearning.DirectML.DML_FEATURE_QUERY_FEATURE_LEVELS_head
    DML_FEATURE_QUERY_FEATURE_LEVELS._fields_ = [
        ('RequestedFeatureLevelCount', UInt32),
        ('RequestedFeatureLevels', POINTER(win32more.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL)),
    ]
    return DML_FEATURE_QUERY_FEATURE_LEVELS
def _define_DML_FEATURE_QUERY_TENSOR_DATA_TYPE_SUPPORT_head():
    class DML_FEATURE_QUERY_TENSOR_DATA_TYPE_SUPPORT(Structure):
        pass
    return DML_FEATURE_QUERY_TENSOR_DATA_TYPE_SUPPORT
def _define_DML_FEATURE_QUERY_TENSOR_DATA_TYPE_SUPPORT():
    DML_FEATURE_QUERY_TENSOR_DATA_TYPE_SUPPORT = win32more.AI.MachineLearning.DirectML.DML_FEATURE_QUERY_TENSOR_DATA_TYPE_SUPPORT_head
    DML_FEATURE_QUERY_TENSOR_DATA_TYPE_SUPPORT._fields_ = [
        ('DataType', win32more.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE),
    ]
    return DML_FEATURE_QUERY_TENSOR_DATA_TYPE_SUPPORT
def _define_DML_FILL_VALUE_CONSTANT_OPERATOR_DESC_head():
    class DML_FILL_VALUE_CONSTANT_OPERATOR_DESC(Structure):
        pass
    return DML_FILL_VALUE_CONSTANT_OPERATOR_DESC
def _define_DML_FILL_VALUE_CONSTANT_OPERATOR_DESC():
    DML_FILL_VALUE_CONSTANT_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_FILL_VALUE_CONSTANT_OPERATOR_DESC_head
    DML_FILL_VALUE_CONSTANT_OPERATOR_DESC._fields_ = [
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ValueDataType', win32more.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE),
        ('Value', win32more.AI.MachineLearning.DirectML.DML_SCALAR_UNION),
    ]
    return DML_FILL_VALUE_CONSTANT_OPERATOR_DESC
def _define_DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC_head():
    class DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC(Structure):
        pass
    return DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC
def _define_DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC():
    DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC_head
    DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC._fields_ = [
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ValueDataType', win32more.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE),
        ('ValueStart', win32more.AI.MachineLearning.DirectML.DML_SCALAR_UNION),
        ('ValueDelta', win32more.AI.MachineLearning.DirectML.DML_SCALAR_UNION),
    ]
    return DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC
def _define_DML_GATHER_ELEMENTS_OPERATOR_DESC_head():
    class DML_GATHER_ELEMENTS_OPERATOR_DESC(Structure):
        pass
    return DML_GATHER_ELEMENTS_OPERATOR_DESC
def _define_DML_GATHER_ELEMENTS_OPERATOR_DESC():
    DML_GATHER_ELEMENTS_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_GATHER_ELEMENTS_OPERATOR_DESC_head
    DML_GATHER_ELEMENTS_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('IndicesTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Axis', UInt32),
    ]
    return DML_GATHER_ELEMENTS_OPERATOR_DESC
def _define_DML_GATHER_ND_OPERATOR_DESC_head():
    class DML_GATHER_ND_OPERATOR_DESC(Structure):
        pass
    return DML_GATHER_ND_OPERATOR_DESC
def _define_DML_GATHER_ND_OPERATOR_DESC():
    DML_GATHER_ND_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_GATHER_ND_OPERATOR_DESC_head
    DML_GATHER_ND_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('IndicesTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InputDimensionCount', UInt32),
        ('IndicesDimensionCount', UInt32),
    ]
    return DML_GATHER_ND_OPERATOR_DESC
def _define_DML_GATHER_ND1_OPERATOR_DESC_head():
    class DML_GATHER_ND1_OPERATOR_DESC(Structure):
        pass
    return DML_GATHER_ND1_OPERATOR_DESC
def _define_DML_GATHER_ND1_OPERATOR_DESC():
    DML_GATHER_ND1_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_GATHER_ND1_OPERATOR_DESC_head
    DML_GATHER_ND1_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('IndicesTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InputDimensionCount', UInt32),
        ('IndicesDimensionCount', UInt32),
        ('BatchDimensionCount', UInt32),
    ]
    return DML_GATHER_ND1_OPERATOR_DESC
def _define_DML_GATHER_OPERATOR_DESC_head():
    class DML_GATHER_OPERATOR_DESC(Structure):
        pass
    return DML_GATHER_OPERATOR_DESC
def _define_DML_GATHER_OPERATOR_DESC():
    DML_GATHER_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_GATHER_OPERATOR_DESC_head
    DML_GATHER_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('IndicesTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Axis', UInt32),
        ('IndexDimensions', UInt32),
    ]
    return DML_GATHER_OPERATOR_DESC
def _define_DML_GEMM_OPERATOR_DESC_head():
    class DML_GEMM_OPERATOR_DESC(Structure):
        pass
    return DML_GEMM_OPERATOR_DESC
def _define_DML_GEMM_OPERATOR_DESC():
    DML_GEMM_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_GEMM_OPERATOR_DESC_head
    DML_GEMM_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('CTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('TransA', win32more.AI.MachineLearning.DirectML.DML_MATRIX_TRANSFORM),
        ('TransB', win32more.AI.MachineLearning.DirectML.DML_MATRIX_TRANSFORM),
        ('Alpha', Single),
        ('Beta', Single),
        ('FusedActivation', POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)),
    ]
    return DML_GEMM_OPERATOR_DESC
def _define_DML_GRAPH_DESC_head():
    class DML_GRAPH_DESC(Structure):
        pass
    return DML_GRAPH_DESC
def _define_DML_GRAPH_DESC():
    DML_GRAPH_DESC = win32more.AI.MachineLearning.DirectML.DML_GRAPH_DESC_head
    DML_GRAPH_DESC._fields_ = [
        ('InputCount', UInt32),
        ('OutputCount', UInt32),
        ('NodeCount', UInt32),
        ('Nodes', POINTER(win32more.AI.MachineLearning.DirectML.DML_GRAPH_NODE_DESC_head)),
        ('InputEdgeCount', UInt32),
        ('InputEdges', POINTER(win32more.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_DESC_head)),
        ('OutputEdgeCount', UInt32),
        ('OutputEdges', POINTER(win32more.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_DESC_head)),
        ('IntermediateEdgeCount', UInt32),
        ('IntermediateEdges', POINTER(win32more.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_DESC_head)),
    ]
    return DML_GRAPH_DESC
def _define_DML_GRAPH_EDGE_DESC_head():
    class DML_GRAPH_EDGE_DESC(Structure):
        pass
    return DML_GRAPH_EDGE_DESC
def _define_DML_GRAPH_EDGE_DESC():
    DML_GRAPH_EDGE_DESC = win32more.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_DESC_head
    DML_GRAPH_EDGE_DESC._fields_ = [
        ('Type', win32more.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_TYPE),
        ('Desc', c_void_p),
    ]
    return DML_GRAPH_EDGE_DESC
DML_GRAPH_EDGE_TYPE = Int32
DML_GRAPH_EDGE_TYPE_INVALID = 0
DML_GRAPH_EDGE_TYPE_INPUT = 1
DML_GRAPH_EDGE_TYPE_OUTPUT = 2
DML_GRAPH_EDGE_TYPE_INTERMEDIATE = 3
def _define_DML_GRAPH_NODE_DESC_head():
    class DML_GRAPH_NODE_DESC(Structure):
        pass
    return DML_GRAPH_NODE_DESC
def _define_DML_GRAPH_NODE_DESC():
    DML_GRAPH_NODE_DESC = win32more.AI.MachineLearning.DirectML.DML_GRAPH_NODE_DESC_head
    DML_GRAPH_NODE_DESC._fields_ = [
        ('Type', win32more.AI.MachineLearning.DirectML.DML_GRAPH_NODE_TYPE),
        ('Desc', c_void_p),
    ]
    return DML_GRAPH_NODE_DESC
DML_GRAPH_NODE_TYPE = Int32
DML_GRAPH_NODE_TYPE_INVALID = 0
DML_GRAPH_NODE_TYPE_OPERATOR = 1
def _define_DML_GRU_OPERATOR_DESC_head():
    class DML_GRU_OPERATOR_DESC(Structure):
        pass
    return DML_GRU_OPERATOR_DESC
def _define_DML_GRU_OPERATOR_DESC():
    DML_GRU_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_GRU_OPERATOR_DESC_head
    DML_GRU_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('WeightTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('RecurrenceTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BiasTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('HiddenInitTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('SequenceLengthsTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputSequenceTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputSingleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ActivationDescCount', UInt32),
        ('ActivationDescs', POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)),
        ('Direction', win32more.AI.MachineLearning.DirectML.DML_RECURRENT_NETWORK_DIRECTION),
        ('LinearBeforeReset', win32more.Foundation.BOOL),
    ]
    return DML_GRU_OPERATOR_DESC
def _define_DML_INPUT_GRAPH_EDGE_DESC_head():
    class DML_INPUT_GRAPH_EDGE_DESC(Structure):
        pass
    return DML_INPUT_GRAPH_EDGE_DESC
def _define_DML_INPUT_GRAPH_EDGE_DESC():
    DML_INPUT_GRAPH_EDGE_DESC = win32more.AI.MachineLearning.DirectML.DML_INPUT_GRAPH_EDGE_DESC_head
    DML_INPUT_GRAPH_EDGE_DESC._fields_ = [
        ('GraphInputIndex', UInt32),
        ('ToNodeIndex', UInt32),
        ('ToNodeInputIndex', UInt32),
        ('Name', win32more.Foundation.PSTR),
    ]
    return DML_INPUT_GRAPH_EDGE_DESC
def _define_DML_INTERMEDIATE_GRAPH_EDGE_DESC_head():
    class DML_INTERMEDIATE_GRAPH_EDGE_DESC(Structure):
        pass
    return DML_INTERMEDIATE_GRAPH_EDGE_DESC
def _define_DML_INTERMEDIATE_GRAPH_EDGE_DESC():
    DML_INTERMEDIATE_GRAPH_EDGE_DESC = win32more.AI.MachineLearning.DirectML.DML_INTERMEDIATE_GRAPH_EDGE_DESC_head
    DML_INTERMEDIATE_GRAPH_EDGE_DESC._fields_ = [
        ('FromNodeIndex', UInt32),
        ('FromNodeOutputIndex', UInt32),
        ('ToNodeIndex', UInt32),
        ('ToNodeInputIndex', UInt32),
        ('Name', win32more.Foundation.PSTR),
    ]
    return DML_INTERMEDIATE_GRAPH_EDGE_DESC
DML_INTERPOLATION_MODE = Int32
DML_INTERPOLATION_MODE_NEAREST_NEIGHBOR = 0
DML_INTERPOLATION_MODE_LINEAR = 1
DML_IS_INFINITY_MODE = Int32
DML_IS_INFINITY_MODE_EITHER = 0
DML_IS_INFINITY_MODE_POSITIVE = 1
DML_IS_INFINITY_MODE_NEGATIVE = 2
def _define_DML_JOIN_OPERATOR_DESC_head():
    class DML_JOIN_OPERATOR_DESC(Structure):
        pass
    return DML_JOIN_OPERATOR_DESC
def _define_DML_JOIN_OPERATOR_DESC():
    DML_JOIN_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_JOIN_OPERATOR_DESC_head
    DML_JOIN_OPERATOR_DESC._fields_ = [
        ('InputCount', UInt32),
        ('InputTensors', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Axis', UInt32),
    ]
    return DML_JOIN_OPERATOR_DESC
def _define_DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC_head():
    class DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC(Structure):
        pass
    return DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC
def _define_DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC():
    DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC_head
    DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InputGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('CrossChannel', win32more.Foundation.BOOL),
        ('LocalSize', UInt32),
        ('Alpha', Single),
        ('Beta', Single),
        ('Bias', Single),
    ]
    return DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC
def _define_DML_LOCAL_RESPONSE_NORMALIZATION_OPERATOR_DESC_head():
    class DML_LOCAL_RESPONSE_NORMALIZATION_OPERATOR_DESC(Structure):
        pass
    return DML_LOCAL_RESPONSE_NORMALIZATION_OPERATOR_DESC
def _define_DML_LOCAL_RESPONSE_NORMALIZATION_OPERATOR_DESC():
    DML_LOCAL_RESPONSE_NORMALIZATION_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_LOCAL_RESPONSE_NORMALIZATION_OPERATOR_DESC_head
    DML_LOCAL_RESPONSE_NORMALIZATION_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('CrossChannel', win32more.Foundation.BOOL),
        ('LocalSize', UInt32),
        ('Alpha', Single),
        ('Beta', Single),
        ('Bias', Single),
    ]
    return DML_LOCAL_RESPONSE_NORMALIZATION_OPERATOR_DESC
def _define_DML_LP_NORMALIZATION_OPERATOR_DESC_head():
    class DML_LP_NORMALIZATION_OPERATOR_DESC(Structure):
        pass
    return DML_LP_NORMALIZATION_OPERATOR_DESC
def _define_DML_LP_NORMALIZATION_OPERATOR_DESC():
    DML_LP_NORMALIZATION_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_LP_NORMALIZATION_OPERATOR_DESC_head
    DML_LP_NORMALIZATION_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Axis', UInt32),
        ('Epsilon', Single),
        ('P', UInt32),
    ]
    return DML_LP_NORMALIZATION_OPERATOR_DESC
def _define_DML_LP_POOLING_OPERATOR_DESC_head():
    class DML_LP_POOLING_OPERATOR_DESC(Structure):
        pass
    return DML_LP_POOLING_OPERATOR_DESC
def _define_DML_LP_POOLING_OPERATOR_DESC():
    DML_LP_POOLING_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_LP_POOLING_OPERATOR_DESC_head
    DML_LP_POOLING_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('DimensionCount', UInt32),
        ('Strides', POINTER(UInt32)),
        ('WindowSize', POINTER(UInt32)),
        ('StartPadding', POINTER(UInt32)),
        ('EndPadding', POINTER(UInt32)),
        ('P', UInt32),
    ]
    return DML_LP_POOLING_OPERATOR_DESC
def _define_DML_LSTM_OPERATOR_DESC_head():
    class DML_LSTM_OPERATOR_DESC(Structure):
        pass
    return DML_LSTM_OPERATOR_DESC
def _define_DML_LSTM_OPERATOR_DESC():
    DML_LSTM_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_LSTM_OPERATOR_DESC_head
    DML_LSTM_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('WeightTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('RecurrenceTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BiasTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('HiddenInitTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('CellMemInitTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('SequenceLengthsTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('PeepholeTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputSequenceTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputSingleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputCellSingleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ActivationDescCount', UInt32),
        ('ActivationDescs', POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)),
        ('Direction', win32more.AI.MachineLearning.DirectML.DML_RECURRENT_NETWORK_DIRECTION),
        ('ClipThreshold', Single),
        ('UseClipThreshold', win32more.Foundation.BOOL),
        ('CoupleInputForget', win32more.Foundation.BOOL),
    ]
    return DML_LSTM_OPERATOR_DESC
def _define_DML_MATRIX_MULTIPLY_INTEGER_OPERATOR_DESC_head():
    class DML_MATRIX_MULTIPLY_INTEGER_OPERATOR_DESC(Structure):
        pass
    return DML_MATRIX_MULTIPLY_INTEGER_OPERATOR_DESC
def _define_DML_MATRIX_MULTIPLY_INTEGER_OPERATOR_DESC():
    DML_MATRIX_MULTIPLY_INTEGER_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_MATRIX_MULTIPLY_INTEGER_OPERATOR_DESC_head
    DML_MATRIX_MULTIPLY_INTEGER_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('AZeroPointTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BZeroPointTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_MATRIX_MULTIPLY_INTEGER_OPERATOR_DESC
DML_MATRIX_TRANSFORM = Int32
DML_MATRIX_TRANSFORM_NONE = 0
DML_MATRIX_TRANSFORM_TRANSPOSE = 1
def _define_DML_MAX_POOLING_GRAD_OPERATOR_DESC_head():
    class DML_MAX_POOLING_GRAD_OPERATOR_DESC(Structure):
        pass
    return DML_MAX_POOLING_GRAD_OPERATOR_DESC
def _define_DML_MAX_POOLING_GRAD_OPERATOR_DESC():
    DML_MAX_POOLING_GRAD_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_MAX_POOLING_GRAD_OPERATOR_DESC_head
    DML_MAX_POOLING_GRAD_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InputGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('DimensionCount', UInt32),
        ('Strides', POINTER(UInt32)),
        ('WindowSize', POINTER(UInt32)),
        ('StartPadding', POINTER(UInt32)),
        ('EndPadding', POINTER(UInt32)),
        ('Dilations', POINTER(UInt32)),
    ]
    return DML_MAX_POOLING_GRAD_OPERATOR_DESC
def _define_DML_MAX_POOLING_OPERATOR_DESC_head():
    class DML_MAX_POOLING_OPERATOR_DESC(Structure):
        pass
    return DML_MAX_POOLING_OPERATOR_DESC
def _define_DML_MAX_POOLING_OPERATOR_DESC():
    DML_MAX_POOLING_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_MAX_POOLING_OPERATOR_DESC_head
    DML_MAX_POOLING_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('DimensionCount', UInt32),
        ('Strides', POINTER(UInt32)),
        ('WindowSize', POINTER(UInt32)),
        ('StartPadding', POINTER(UInt32)),
        ('EndPadding', POINTER(UInt32)),
    ]
    return DML_MAX_POOLING_OPERATOR_DESC
def _define_DML_MAX_POOLING1_OPERATOR_DESC_head():
    class DML_MAX_POOLING1_OPERATOR_DESC(Structure):
        pass
    return DML_MAX_POOLING1_OPERATOR_DESC
def _define_DML_MAX_POOLING1_OPERATOR_DESC():
    DML_MAX_POOLING1_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_MAX_POOLING1_OPERATOR_DESC_head
    DML_MAX_POOLING1_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputIndicesTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('DimensionCount', UInt32),
        ('Strides', POINTER(UInt32)),
        ('WindowSize', POINTER(UInt32)),
        ('StartPadding', POINTER(UInt32)),
        ('EndPadding', POINTER(UInt32)),
    ]
    return DML_MAX_POOLING1_OPERATOR_DESC
def _define_DML_MAX_POOLING2_OPERATOR_DESC_head():
    class DML_MAX_POOLING2_OPERATOR_DESC(Structure):
        pass
    return DML_MAX_POOLING2_OPERATOR_DESC
def _define_DML_MAX_POOLING2_OPERATOR_DESC():
    DML_MAX_POOLING2_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_MAX_POOLING2_OPERATOR_DESC_head
    DML_MAX_POOLING2_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputIndicesTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('DimensionCount', UInt32),
        ('Strides', POINTER(UInt32)),
        ('WindowSize', POINTER(UInt32)),
        ('StartPadding', POINTER(UInt32)),
        ('EndPadding', POINTER(UInt32)),
        ('Dilations', POINTER(UInt32)),
    ]
    return DML_MAX_POOLING2_OPERATOR_DESC
def _define_DML_MAX_UNPOOLING_OPERATOR_DESC_head():
    class DML_MAX_UNPOOLING_OPERATOR_DESC(Structure):
        pass
    return DML_MAX_UNPOOLING_OPERATOR_DESC
def _define_DML_MAX_UNPOOLING_OPERATOR_DESC():
    DML_MAX_UNPOOLING_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_MAX_UNPOOLING_OPERATOR_DESC_head
    DML_MAX_UNPOOLING_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('IndicesTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_MAX_UNPOOLING_OPERATOR_DESC
def _define_DML_MEAN_VARIANCE_NORMALIZATION_OPERATOR_DESC_head():
    class DML_MEAN_VARIANCE_NORMALIZATION_OPERATOR_DESC(Structure):
        pass
    return DML_MEAN_VARIANCE_NORMALIZATION_OPERATOR_DESC
def _define_DML_MEAN_VARIANCE_NORMALIZATION_OPERATOR_DESC():
    DML_MEAN_VARIANCE_NORMALIZATION_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_MEAN_VARIANCE_NORMALIZATION_OPERATOR_DESC_head
    DML_MEAN_VARIANCE_NORMALIZATION_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BiasTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('CrossChannel', win32more.Foundation.BOOL),
        ('NormalizeVariance', win32more.Foundation.BOOL),
        ('Epsilon', Single),
        ('FusedActivation', POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)),
    ]
    return DML_MEAN_VARIANCE_NORMALIZATION_OPERATOR_DESC
def _define_DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC_head():
    class DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC(Structure):
        pass
    return DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC
def _define_DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC():
    DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC_head
    DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BiasTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('AxisCount', UInt32),
        ('Axes', POINTER(UInt32)),
        ('NormalizeVariance', win32more.Foundation.BOOL),
        ('Epsilon', Single),
        ('FusedActivation', POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)),
    ]
    return DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC
def _define_DML_NONZERO_COORDINATES_OPERATOR_DESC_head():
    class DML_NONZERO_COORDINATES_OPERATOR_DESC(Structure):
        pass
    return DML_NONZERO_COORDINATES_OPERATOR_DESC
def _define_DML_NONZERO_COORDINATES_OPERATOR_DESC():
    DML_NONZERO_COORDINATES_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_NONZERO_COORDINATES_OPERATOR_DESC_head
    DML_NONZERO_COORDINATES_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputCountTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputCoordinatesTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_NONZERO_COORDINATES_OPERATOR_DESC
def _define_DML_ONE_HOT_OPERATOR_DESC_head():
    class DML_ONE_HOT_OPERATOR_DESC(Structure):
        pass
    return DML_ONE_HOT_OPERATOR_DESC
def _define_DML_ONE_HOT_OPERATOR_DESC():
    DML_ONE_HOT_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ONE_HOT_OPERATOR_DESC_head
    DML_ONE_HOT_OPERATOR_DESC._fields_ = [
        ('IndicesTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ValuesTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Axis', UInt32),
    ]
    return DML_ONE_HOT_OPERATOR_DESC
def _define_DML_OPERATOR_DESC_head():
    class DML_OPERATOR_DESC(Structure):
        pass
    return DML_OPERATOR_DESC
def _define_DML_OPERATOR_DESC():
    DML_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head
    DML_OPERATOR_DESC._fields_ = [
        ('Type', win32more.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE),
        ('Desc', c_void_p),
    ]
    return DML_OPERATOR_DESC
def _define_DML_OPERATOR_GRAPH_NODE_DESC_head():
    class DML_OPERATOR_GRAPH_NODE_DESC(Structure):
        pass
    return DML_OPERATOR_GRAPH_NODE_DESC
def _define_DML_OPERATOR_GRAPH_NODE_DESC():
    DML_OPERATOR_GRAPH_NODE_DESC = win32more.AI.MachineLearning.DirectML.DML_OPERATOR_GRAPH_NODE_DESC_head
    DML_OPERATOR_GRAPH_NODE_DESC._fields_ = [
        ('Operator', win32more.AI.MachineLearning.DirectML.IDMLOperator_head),
        ('Name', win32more.Foundation.PSTR),
    ]
    return DML_OPERATOR_GRAPH_NODE_DESC
DML_OPERATOR_TYPE = Int32
DML_OPERATOR_INVALID = 0
DML_OPERATOR_ELEMENT_WISE_IDENTITY = 1
DML_OPERATOR_ELEMENT_WISE_ABS = 2
DML_OPERATOR_ELEMENT_WISE_ACOS = 3
DML_OPERATOR_ELEMENT_WISE_ADD = 4
DML_OPERATOR_ELEMENT_WISE_ASIN = 5
DML_OPERATOR_ELEMENT_WISE_ATAN = 6
DML_OPERATOR_ELEMENT_WISE_CEIL = 7
DML_OPERATOR_ELEMENT_WISE_CLIP = 8
DML_OPERATOR_ELEMENT_WISE_COS = 9
DML_OPERATOR_ELEMENT_WISE_DIVIDE = 10
DML_OPERATOR_ELEMENT_WISE_EXP = 11
DML_OPERATOR_ELEMENT_WISE_FLOOR = 12
DML_OPERATOR_ELEMENT_WISE_LOG = 13
DML_OPERATOR_ELEMENT_WISE_LOGICAL_AND = 14
DML_OPERATOR_ELEMENT_WISE_LOGICAL_EQUALS = 15
DML_OPERATOR_ELEMENT_WISE_LOGICAL_GREATER_THAN = 16
DML_OPERATOR_ELEMENT_WISE_LOGICAL_LESS_THAN = 17
DML_OPERATOR_ELEMENT_WISE_LOGICAL_NOT = 18
DML_OPERATOR_ELEMENT_WISE_LOGICAL_OR = 19
DML_OPERATOR_ELEMENT_WISE_LOGICAL_XOR = 20
DML_OPERATOR_ELEMENT_WISE_MAX = 21
DML_OPERATOR_ELEMENT_WISE_MEAN = 22
DML_OPERATOR_ELEMENT_WISE_MIN = 23
DML_OPERATOR_ELEMENT_WISE_MULTIPLY = 24
DML_OPERATOR_ELEMENT_WISE_POW = 25
DML_OPERATOR_ELEMENT_WISE_CONSTANT_POW = 26
DML_OPERATOR_ELEMENT_WISE_RECIP = 27
DML_OPERATOR_ELEMENT_WISE_SIN = 28
DML_OPERATOR_ELEMENT_WISE_SQRT = 29
DML_OPERATOR_ELEMENT_WISE_SUBTRACT = 30
DML_OPERATOR_ELEMENT_WISE_TAN = 31
DML_OPERATOR_ELEMENT_WISE_THRESHOLD = 32
DML_OPERATOR_ELEMENT_WISE_QUANTIZE_LINEAR = 33
DML_OPERATOR_ELEMENT_WISE_DEQUANTIZE_LINEAR = 34
DML_OPERATOR_ACTIVATION_ELU = 35
DML_OPERATOR_ACTIVATION_HARDMAX = 36
DML_OPERATOR_ACTIVATION_HARD_SIGMOID = 37
DML_OPERATOR_ACTIVATION_IDENTITY = 38
DML_OPERATOR_ACTIVATION_LEAKY_RELU = 39
DML_OPERATOR_ACTIVATION_LINEAR = 40
DML_OPERATOR_ACTIVATION_LOG_SOFTMAX = 41
DML_OPERATOR_ACTIVATION_PARAMETERIZED_RELU = 42
DML_OPERATOR_ACTIVATION_PARAMETRIC_SOFTPLUS = 43
DML_OPERATOR_ACTIVATION_RELU = 44
DML_OPERATOR_ACTIVATION_SCALED_ELU = 45
DML_OPERATOR_ACTIVATION_SCALED_TANH = 46
DML_OPERATOR_ACTIVATION_SIGMOID = 47
DML_OPERATOR_ACTIVATION_SOFTMAX = 48
DML_OPERATOR_ACTIVATION_SOFTPLUS = 49
DML_OPERATOR_ACTIVATION_SOFTSIGN = 50
DML_OPERATOR_ACTIVATION_TANH = 51
DML_OPERATOR_ACTIVATION_THRESHOLDED_RELU = 52
DML_OPERATOR_CONVOLUTION = 53
DML_OPERATOR_GEMM = 54
DML_OPERATOR_REDUCE = 55
DML_OPERATOR_AVERAGE_POOLING = 56
DML_OPERATOR_LP_POOLING = 57
DML_OPERATOR_MAX_POOLING = 58
DML_OPERATOR_ROI_POOLING = 59
DML_OPERATOR_SLICE = 60
DML_OPERATOR_CAST = 61
DML_OPERATOR_SPLIT = 62
DML_OPERATOR_JOIN = 63
DML_OPERATOR_PADDING = 64
DML_OPERATOR_VALUE_SCALE_2D = 65
DML_OPERATOR_UPSAMPLE_2D = 66
DML_OPERATOR_GATHER = 67
DML_OPERATOR_SPACE_TO_DEPTH = 68
DML_OPERATOR_DEPTH_TO_SPACE = 69
DML_OPERATOR_TILE = 70
DML_OPERATOR_TOP_K = 71
DML_OPERATOR_BATCH_NORMALIZATION = 72
DML_OPERATOR_MEAN_VARIANCE_NORMALIZATION = 73
DML_OPERATOR_LOCAL_RESPONSE_NORMALIZATION = 74
DML_OPERATOR_LP_NORMALIZATION = 75
DML_OPERATOR_RNN = 76
DML_OPERATOR_LSTM = 77
DML_OPERATOR_GRU = 78
DML_OPERATOR_ELEMENT_WISE_SIGN = 79
DML_OPERATOR_ELEMENT_WISE_IS_NAN = 80
DML_OPERATOR_ELEMENT_WISE_ERF = 81
DML_OPERATOR_ELEMENT_WISE_SINH = 82
DML_OPERATOR_ELEMENT_WISE_COSH = 83
DML_OPERATOR_ELEMENT_WISE_TANH = 84
DML_OPERATOR_ELEMENT_WISE_ASINH = 85
DML_OPERATOR_ELEMENT_WISE_ACOSH = 86
DML_OPERATOR_ELEMENT_WISE_ATANH = 87
DML_OPERATOR_ELEMENT_WISE_IF = 88
DML_OPERATOR_ELEMENT_WISE_ADD1 = 89
DML_OPERATOR_ACTIVATION_SHRINK = 90
DML_OPERATOR_MAX_POOLING1 = 91
DML_OPERATOR_MAX_UNPOOLING = 92
DML_OPERATOR_DIAGONAL_MATRIX = 93
DML_OPERATOR_SCATTER_ELEMENTS = 94
DML_OPERATOR_SCATTER = 94
DML_OPERATOR_ONE_HOT = 95
DML_OPERATOR_RESAMPLE = 96
DML_OPERATOR_ELEMENT_WISE_BIT_SHIFT_LEFT = 97
DML_OPERATOR_ELEMENT_WISE_BIT_SHIFT_RIGHT = 98
DML_OPERATOR_ELEMENT_WISE_ROUND = 99
DML_OPERATOR_ELEMENT_WISE_IS_INFINITY = 100
DML_OPERATOR_ELEMENT_WISE_MODULUS_TRUNCATE = 101
DML_OPERATOR_ELEMENT_WISE_MODULUS_FLOOR = 102
DML_OPERATOR_FILL_VALUE_CONSTANT = 103
DML_OPERATOR_FILL_VALUE_SEQUENCE = 104
DML_OPERATOR_CUMULATIVE_SUMMATION = 105
DML_OPERATOR_REVERSE_SUBSEQUENCES = 106
DML_OPERATOR_GATHER_ELEMENTS = 107
DML_OPERATOR_GATHER_ND = 108
DML_OPERATOR_SCATTER_ND = 109
DML_OPERATOR_MAX_POOLING2 = 110
DML_OPERATOR_SLICE1 = 111
DML_OPERATOR_TOP_K1 = 112
DML_OPERATOR_DEPTH_TO_SPACE1 = 113
DML_OPERATOR_SPACE_TO_DEPTH1 = 114
DML_OPERATOR_MEAN_VARIANCE_NORMALIZATION1 = 115
DML_OPERATOR_RESAMPLE1 = 116
DML_OPERATOR_MATRIX_MULTIPLY_INTEGER = 117
DML_OPERATOR_QUANTIZED_LINEAR_MATRIX_MULTIPLY = 118
DML_OPERATOR_CONVOLUTION_INTEGER = 119
DML_OPERATOR_QUANTIZED_LINEAR_CONVOLUTION = 120
DML_OPERATOR_ELEMENT_WISE_BIT_AND = 121
DML_OPERATOR_ELEMENT_WISE_BIT_OR = 122
DML_OPERATOR_ELEMENT_WISE_BIT_XOR = 123
DML_OPERATOR_ELEMENT_WISE_BIT_NOT = 124
DML_OPERATOR_ELEMENT_WISE_BIT_COUNT = 125
DML_OPERATOR_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL = 126
DML_OPERATOR_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL = 127
DML_OPERATOR_ACTIVATION_CELU = 128
DML_OPERATOR_ACTIVATION_RELU_GRAD = 129
DML_OPERATOR_AVERAGE_POOLING_GRAD = 130
DML_OPERATOR_MAX_POOLING_GRAD = 131
DML_OPERATOR_RANDOM_GENERATOR = 132
DML_OPERATOR_NONZERO_COORDINATES = 133
DML_OPERATOR_RESAMPLE_GRAD = 134
DML_OPERATOR_SLICE_GRAD = 135
DML_OPERATOR_ADAM_OPTIMIZER = 136
DML_OPERATOR_ARGMIN = 137
DML_OPERATOR_ARGMAX = 138
DML_OPERATOR_ROI_ALIGN = 139
DML_OPERATOR_GATHER_ND1 = 140
DML_OPERATOR_ELEMENT_WISE_ATAN_YX = 141
DML_OPERATOR_ELEMENT_WISE_CLIP_GRAD = 142
DML_OPERATOR_ELEMENT_WISE_DIFFERENCE_SQUARE = 143
DML_OPERATOR_LOCAL_RESPONSE_NORMALIZATION_GRAD = 144
DML_OPERATOR_CUMULATIVE_PRODUCT = 145
DML_OPERATOR_BATCH_NORMALIZATION_GRAD = 146
DML_OPERATOR_ELEMENT_WISE_QUANTIZED_LINEAR_ADD = 147
DML_OPERATOR_DYNAMIC_QUANTIZE_LINEAR = 148
DML_OPERATOR_ROI_ALIGN1 = 149
def _define_DML_OUTPUT_GRAPH_EDGE_DESC_head():
    class DML_OUTPUT_GRAPH_EDGE_DESC(Structure):
        pass
    return DML_OUTPUT_GRAPH_EDGE_DESC
def _define_DML_OUTPUT_GRAPH_EDGE_DESC():
    DML_OUTPUT_GRAPH_EDGE_DESC = win32more.AI.MachineLearning.DirectML.DML_OUTPUT_GRAPH_EDGE_DESC_head
    DML_OUTPUT_GRAPH_EDGE_DESC._fields_ = [
        ('FromNodeIndex', UInt32),
        ('FromNodeOutputIndex', UInt32),
        ('GraphOutputIndex', UInt32),
        ('Name', win32more.Foundation.PSTR),
    ]
    return DML_OUTPUT_GRAPH_EDGE_DESC
DML_PADDING_MODE = Int32
DML_PADDING_MODE_CONSTANT = 0
DML_PADDING_MODE_EDGE = 1
DML_PADDING_MODE_REFLECTION = 2
DML_PADDING_MODE_SYMMETRIC = 3
def _define_DML_PADDING_OPERATOR_DESC_head():
    class DML_PADDING_OPERATOR_DESC(Structure):
        pass
    return DML_PADDING_OPERATOR_DESC
def _define_DML_PADDING_OPERATOR_DESC():
    DML_PADDING_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_PADDING_OPERATOR_DESC_head
    DML_PADDING_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('PaddingMode', win32more.AI.MachineLearning.DirectML.DML_PADDING_MODE),
        ('PaddingValue', Single),
        ('DimensionCount', UInt32),
        ('StartPadding', POINTER(UInt32)),
        ('EndPadding', POINTER(UInt32)),
    ]
    return DML_PADDING_OPERATOR_DESC
def _define_DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC_head():
    class DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC(Structure):
        pass
    return DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC
def _define_DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC():
    DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC_head
    DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InputScaleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InputZeroPointTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('FilterTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('FilterScaleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('FilterZeroPointTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BiasTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputScaleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputZeroPointTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('DimensionCount', UInt32),
        ('Strides', POINTER(UInt32)),
        ('Dilations', POINTER(UInt32)),
        ('StartPadding', POINTER(UInt32)),
        ('EndPadding', POINTER(UInt32)),
        ('GroupCount', UInt32),
    ]
    return DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC
def _define_DML_QUANTIZED_LINEAR_MATRIX_MULTIPLY_OPERATOR_DESC_head():
    class DML_QUANTIZED_LINEAR_MATRIX_MULTIPLY_OPERATOR_DESC(Structure):
        pass
    return DML_QUANTIZED_LINEAR_MATRIX_MULTIPLY_OPERATOR_DESC
def _define_DML_QUANTIZED_LINEAR_MATRIX_MULTIPLY_OPERATOR_DESC():
    DML_QUANTIZED_LINEAR_MATRIX_MULTIPLY_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_QUANTIZED_LINEAR_MATRIX_MULTIPLY_OPERATOR_DESC_head
    DML_QUANTIZED_LINEAR_MATRIX_MULTIPLY_OPERATOR_DESC._fields_ = [
        ('ATensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('AScaleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('AZeroPointTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BScaleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BZeroPointTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputScaleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputZeroPointTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
    ]
    return DML_QUANTIZED_LINEAR_MATRIX_MULTIPLY_OPERATOR_DESC
def _define_DML_RANDOM_GENERATOR_OPERATOR_DESC_head():
    class DML_RANDOM_GENERATOR_OPERATOR_DESC(Structure):
        pass
    return DML_RANDOM_GENERATOR_OPERATOR_DESC
def _define_DML_RANDOM_GENERATOR_OPERATOR_DESC():
    DML_RANDOM_GENERATOR_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_RANDOM_GENERATOR_OPERATOR_DESC_head
    DML_RANDOM_GENERATOR_OPERATOR_DESC._fields_ = [
        ('InputStateTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputStateTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Type', win32more.AI.MachineLearning.DirectML.DML_RANDOM_GENERATOR_TYPE),
    ]
    return DML_RANDOM_GENERATOR_OPERATOR_DESC
DML_RANDOM_GENERATOR_TYPE = Int32
DML_RANDOM_GENERATOR_TYPE_PHILOX_4X32_10 = 0
DML_RECURRENT_NETWORK_DIRECTION = Int32
DML_RECURRENT_NETWORK_DIRECTION_FORWARD = 0
DML_RECURRENT_NETWORK_DIRECTION_BACKWARD = 1
DML_RECURRENT_NETWORK_DIRECTION_BIDIRECTIONAL = 2
DML_REDUCE_FUNCTION = Int32
DML_REDUCE_FUNCTION_ARGMAX = 0
DML_REDUCE_FUNCTION_ARGMIN = 1
DML_REDUCE_FUNCTION_AVERAGE = 2
DML_REDUCE_FUNCTION_L1 = 3
DML_REDUCE_FUNCTION_L2 = 4
DML_REDUCE_FUNCTION_LOG_SUM = 5
DML_REDUCE_FUNCTION_LOG_SUM_EXP = 6
DML_REDUCE_FUNCTION_MAX = 7
DML_REDUCE_FUNCTION_MIN = 8
DML_REDUCE_FUNCTION_MULTIPLY = 9
DML_REDUCE_FUNCTION_SUM = 10
DML_REDUCE_FUNCTION_SUM_SQUARE = 11
def _define_DML_REDUCE_OPERATOR_DESC_head():
    class DML_REDUCE_OPERATOR_DESC(Structure):
        pass
    return DML_REDUCE_OPERATOR_DESC
def _define_DML_REDUCE_OPERATOR_DESC():
    DML_REDUCE_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_REDUCE_OPERATOR_DESC_head
    DML_REDUCE_OPERATOR_DESC._fields_ = [
        ('Function', win32more.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION),
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('AxisCount', UInt32),
        ('Axes', POINTER(UInt32)),
    ]
    return DML_REDUCE_OPERATOR_DESC
def _define_DML_RESAMPLE_GRAD_OPERATOR_DESC_head():
    class DML_RESAMPLE_GRAD_OPERATOR_DESC(Structure):
        pass
    return DML_RESAMPLE_GRAD_OPERATOR_DESC
def _define_DML_RESAMPLE_GRAD_OPERATOR_DESC():
    DML_RESAMPLE_GRAD_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_RESAMPLE_GRAD_OPERATOR_DESC_head
    DML_RESAMPLE_GRAD_OPERATOR_DESC._fields_ = [
        ('InputGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InterpolationMode', win32more.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE),
        ('DimensionCount', UInt32),
        ('Scales', POINTER(Single)),
        ('InputPixelOffsets', POINTER(Single)),
        ('OutputPixelOffsets', POINTER(Single)),
    ]
    return DML_RESAMPLE_GRAD_OPERATOR_DESC
def _define_DML_RESAMPLE_OPERATOR_DESC_head():
    class DML_RESAMPLE_OPERATOR_DESC(Structure):
        pass
    return DML_RESAMPLE_OPERATOR_DESC
def _define_DML_RESAMPLE_OPERATOR_DESC():
    DML_RESAMPLE_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_RESAMPLE_OPERATOR_DESC_head
    DML_RESAMPLE_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InterpolationMode', win32more.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE),
        ('ScaleCount', UInt32),
        ('Scales', POINTER(Single)),
    ]
    return DML_RESAMPLE_OPERATOR_DESC
def _define_DML_RESAMPLE1_OPERATOR_DESC_head():
    class DML_RESAMPLE1_OPERATOR_DESC(Structure):
        pass
    return DML_RESAMPLE1_OPERATOR_DESC
def _define_DML_RESAMPLE1_OPERATOR_DESC():
    DML_RESAMPLE1_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_RESAMPLE1_OPERATOR_DESC_head
    DML_RESAMPLE1_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InterpolationMode', win32more.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE),
        ('DimensionCount', UInt32),
        ('Scales', POINTER(Single)),
        ('InputPixelOffsets', POINTER(Single)),
        ('OutputPixelOffsets', POINTER(Single)),
    ]
    return DML_RESAMPLE1_OPERATOR_DESC
def _define_DML_REVERSE_SUBSEQUENCES_OPERATOR_DESC_head():
    class DML_REVERSE_SUBSEQUENCES_OPERATOR_DESC(Structure):
        pass
    return DML_REVERSE_SUBSEQUENCES_OPERATOR_DESC
def _define_DML_REVERSE_SUBSEQUENCES_OPERATOR_DESC():
    DML_REVERSE_SUBSEQUENCES_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_REVERSE_SUBSEQUENCES_OPERATOR_DESC_head
    DML_REVERSE_SUBSEQUENCES_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('SequenceLengthsTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Axis', UInt32),
    ]
    return DML_REVERSE_SUBSEQUENCES_OPERATOR_DESC
def _define_DML_RNN_OPERATOR_DESC_head():
    class DML_RNN_OPERATOR_DESC(Structure):
        pass
    return DML_RNN_OPERATOR_DESC
def _define_DML_RNN_OPERATOR_DESC():
    DML_RNN_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_RNN_OPERATOR_DESC_head
    DML_RNN_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('WeightTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('RecurrenceTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BiasTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('HiddenInitTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('SequenceLengthsTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputSequenceTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputSingleTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ActivationDescCount', UInt32),
        ('ActivationDescs', POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)),
        ('Direction', win32more.AI.MachineLearning.DirectML.DML_RECURRENT_NETWORK_DIRECTION),
    ]
    return DML_RNN_OPERATOR_DESC
def _define_DML_ROI_ALIGN_OPERATOR_DESC_head():
    class DML_ROI_ALIGN_OPERATOR_DESC(Structure):
        pass
    return DML_ROI_ALIGN_OPERATOR_DESC
def _define_DML_ROI_ALIGN_OPERATOR_DESC():
    DML_ROI_ALIGN_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ROI_ALIGN_OPERATOR_DESC_head
    DML_ROI_ALIGN_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ROITensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BatchIndicesTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ReductionFunction', win32more.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION),
        ('InterpolationMode', win32more.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE),
        ('SpatialScaleX', Single),
        ('SpatialScaleY', Single),
        ('OutOfBoundsInputValue', Single),
        ('MinimumSamplesPerOutput', UInt32),
        ('MaximumSamplesPerOutput', UInt32),
    ]
    return DML_ROI_ALIGN_OPERATOR_DESC
def _define_DML_ROI_ALIGN1_OPERATOR_DESC_head():
    class DML_ROI_ALIGN1_OPERATOR_DESC(Structure):
        pass
    return DML_ROI_ALIGN1_OPERATOR_DESC
def _define_DML_ROI_ALIGN1_OPERATOR_DESC():
    DML_ROI_ALIGN1_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ROI_ALIGN1_OPERATOR_DESC_head
    DML_ROI_ALIGN1_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ROITensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BatchIndicesTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ReductionFunction', win32more.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION),
        ('InterpolationMode', win32more.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE),
        ('SpatialScaleX', Single),
        ('SpatialScaleY', Single),
        ('InputPixelOffset', Single),
        ('OutputPixelOffset', Single),
        ('OutOfBoundsInputValue', Single),
        ('MinimumSamplesPerOutput', UInt32),
        ('MaximumSamplesPerOutput', UInt32),
        ('AlignRegionsToCorners', win32more.Foundation.BOOL),
    ]
    return DML_ROI_ALIGN1_OPERATOR_DESC
def _define_DML_ROI_POOLING_OPERATOR_DESC_head():
    class DML_ROI_POOLING_OPERATOR_DESC(Structure):
        pass
    return DML_ROI_POOLING_OPERATOR_DESC
def _define_DML_ROI_POOLING_OPERATOR_DESC():
    DML_ROI_POOLING_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_ROI_POOLING_OPERATOR_DESC_head
    DML_ROI_POOLING_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ROITensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('SpatialScale', Single),
        ('PooledSize', win32more.AI.MachineLearning.DirectML.DML_SIZE_2D),
    ]
    return DML_ROI_POOLING_OPERATOR_DESC
DML_ROUNDING_MODE = Int32
DML_ROUNDING_MODE_HALVES_TO_NEAREST_EVEN = 0
DML_ROUNDING_MODE_TOWARD_ZERO = 1
DML_ROUNDING_MODE_TOWARD_INFINITY = 2
def _define_DML_SCALAR_UNION_head():
    class DML_SCALAR_UNION(Union):
        pass
    return DML_SCALAR_UNION
def _define_DML_SCALAR_UNION():
    DML_SCALAR_UNION = win32more.AI.MachineLearning.DirectML.DML_SCALAR_UNION_head
    DML_SCALAR_UNION._fields_ = [
        ('Bytes', Byte * 8),
        ('Int8', SByte),
        ('UInt8', Byte),
        ('Int16', Int16),
        ('UInt16', UInt16),
        ('Int32', Int32),
        ('UInt32', UInt32),
        ('Int64', Int64),
        ('UInt64', UInt64),
        ('Float32', Single),
        ('Float64', Double),
    ]
    return DML_SCALAR_UNION
def _define_DML_SCALE_BIAS_head():
    class DML_SCALE_BIAS(Structure):
        pass
    return DML_SCALE_BIAS
def _define_DML_SCALE_BIAS():
    DML_SCALE_BIAS = win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head
    DML_SCALE_BIAS._fields_ = [
        ('Scale', Single),
        ('Bias', Single),
    ]
    return DML_SCALE_BIAS
def _define_DML_SCATTER_ND_OPERATOR_DESC_head():
    class DML_SCATTER_ND_OPERATOR_DESC(Structure):
        pass
    return DML_SCATTER_ND_OPERATOR_DESC
def _define_DML_SCATTER_ND_OPERATOR_DESC():
    DML_SCATTER_ND_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_SCATTER_ND_OPERATOR_DESC_head
    DML_SCATTER_ND_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('IndicesTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('UpdatesTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('InputDimensionCount', UInt32),
        ('IndicesDimensionCount', UInt32),
    ]
    return DML_SCATTER_ND_OPERATOR_DESC
def _define_DML_SCATTER_OPERATOR_DESC_head():
    class DML_SCATTER_OPERATOR_DESC(Structure):
        pass
    return DML_SCATTER_OPERATOR_DESC
def _define_DML_SCATTER_OPERATOR_DESC():
    DML_SCATTER_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_SCATTER_OPERATOR_DESC_head
    DML_SCATTER_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('IndicesTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('UpdatesTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Axis', UInt32),
    ]
    return DML_SCATTER_OPERATOR_DESC
def _define_DML_SIZE_2D_head():
    class DML_SIZE_2D(Structure):
        pass
    return DML_SIZE_2D
def _define_DML_SIZE_2D():
    DML_SIZE_2D = win32more.AI.MachineLearning.DirectML.DML_SIZE_2D_head
    DML_SIZE_2D._fields_ = [
        ('Width', UInt32),
        ('Height', UInt32),
    ]
    return DML_SIZE_2D
def _define_DML_SLICE_GRAD_OPERATOR_DESC_head():
    class DML_SLICE_GRAD_OPERATOR_DESC(Structure):
        pass
    return DML_SLICE_GRAD_OPERATOR_DESC
def _define_DML_SLICE_GRAD_OPERATOR_DESC():
    DML_SLICE_GRAD_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_SLICE_GRAD_OPERATOR_DESC_head
    DML_SLICE_GRAD_OPERATOR_DESC._fields_ = [
        ('InputGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputGradientTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('DimensionCount', UInt32),
        ('InputWindowOffsets', POINTER(UInt32)),
        ('InputWindowSizes', POINTER(UInt32)),
        ('InputWindowStrides', POINTER(Int32)),
    ]
    return DML_SLICE_GRAD_OPERATOR_DESC
def _define_DML_SLICE_OPERATOR_DESC_head():
    class DML_SLICE_OPERATOR_DESC(Structure):
        pass
    return DML_SLICE_OPERATOR_DESC
def _define_DML_SLICE_OPERATOR_DESC():
    DML_SLICE_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_SLICE_OPERATOR_DESC_head
    DML_SLICE_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('DimensionCount', UInt32),
        ('Offsets', POINTER(UInt32)),
        ('Sizes', POINTER(UInt32)),
        ('Strides', POINTER(UInt32)),
    ]
    return DML_SLICE_OPERATOR_DESC
def _define_DML_SLICE1_OPERATOR_DESC_head():
    class DML_SLICE1_OPERATOR_DESC(Structure):
        pass
    return DML_SLICE1_OPERATOR_DESC
def _define_DML_SLICE1_OPERATOR_DESC():
    DML_SLICE1_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_SLICE1_OPERATOR_DESC_head
    DML_SLICE1_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('DimensionCount', UInt32),
        ('InputWindowOffsets', POINTER(UInt32)),
        ('InputWindowSizes', POINTER(UInt32)),
        ('InputWindowStrides', POINTER(Int32)),
    ]
    return DML_SLICE1_OPERATOR_DESC
def _define_DML_SPACE_TO_DEPTH_OPERATOR_DESC_head():
    class DML_SPACE_TO_DEPTH_OPERATOR_DESC(Structure):
        pass
    return DML_SPACE_TO_DEPTH_OPERATOR_DESC
def _define_DML_SPACE_TO_DEPTH_OPERATOR_DESC():
    DML_SPACE_TO_DEPTH_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_SPACE_TO_DEPTH_OPERATOR_DESC_head
    DML_SPACE_TO_DEPTH_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BlockSize', UInt32),
    ]
    return DML_SPACE_TO_DEPTH_OPERATOR_DESC
def _define_DML_SPACE_TO_DEPTH1_OPERATOR_DESC_head():
    class DML_SPACE_TO_DEPTH1_OPERATOR_DESC(Structure):
        pass
    return DML_SPACE_TO_DEPTH1_OPERATOR_DESC
def _define_DML_SPACE_TO_DEPTH1_OPERATOR_DESC():
    DML_SPACE_TO_DEPTH1_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_SPACE_TO_DEPTH1_OPERATOR_DESC_head
    DML_SPACE_TO_DEPTH1_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('BlockSize', UInt32),
        ('Order', win32more.AI.MachineLearning.DirectML.DML_DEPTH_SPACE_ORDER),
    ]
    return DML_SPACE_TO_DEPTH1_OPERATOR_DESC
def _define_DML_SPLIT_OPERATOR_DESC_head():
    class DML_SPLIT_OPERATOR_DESC(Structure):
        pass
    return DML_SPLIT_OPERATOR_DESC
def _define_DML_SPLIT_OPERATOR_DESC():
    DML_SPLIT_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_SPLIT_OPERATOR_DESC_head
    DML_SPLIT_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputCount', UInt32),
        ('OutputTensors', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Axis', UInt32),
    ]
    return DML_SPLIT_OPERATOR_DESC
DML_TENSOR_DATA_TYPE = Int32
DML_TENSOR_DATA_TYPE_UNKNOWN = 0
DML_TENSOR_DATA_TYPE_FLOAT32 = 1
DML_TENSOR_DATA_TYPE_FLOAT16 = 2
DML_TENSOR_DATA_TYPE_UINT32 = 3
DML_TENSOR_DATA_TYPE_UINT16 = 4
DML_TENSOR_DATA_TYPE_UINT8 = 5
DML_TENSOR_DATA_TYPE_INT32 = 6
DML_TENSOR_DATA_TYPE_INT16 = 7
DML_TENSOR_DATA_TYPE_INT8 = 8
DML_TENSOR_DATA_TYPE_FLOAT64 = 9
DML_TENSOR_DATA_TYPE_UINT64 = 10
DML_TENSOR_DATA_TYPE_INT64 = 11
def _define_DML_TENSOR_DESC_head():
    class DML_TENSOR_DESC(Structure):
        pass
    return DML_TENSOR_DESC
def _define_DML_TENSOR_DESC():
    DML_TENSOR_DESC = win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head
    DML_TENSOR_DESC._fields_ = [
        ('Type', win32more.AI.MachineLearning.DirectML.DML_TENSOR_TYPE),
        ('Desc', c_void_p),
    ]
    return DML_TENSOR_DESC
DML_TENSOR_FLAGS = UInt32
DML_TENSOR_FLAG_NONE = 0
DML_TENSOR_FLAG_OWNED_BY_DML = 1
DML_TENSOR_TYPE = Int32
DML_TENSOR_TYPE_INVALID = 0
DML_TENSOR_TYPE_BUFFER = 1
def _define_DML_TILE_OPERATOR_DESC_head():
    class DML_TILE_OPERATOR_DESC(Structure):
        pass
    return DML_TILE_OPERATOR_DESC
def _define_DML_TILE_OPERATOR_DESC():
    DML_TILE_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_TILE_OPERATOR_DESC_head
    DML_TILE_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('RepeatsCount', UInt32),
        ('Repeats', POINTER(UInt32)),
    ]
    return DML_TILE_OPERATOR_DESC
def _define_DML_TOP_K_OPERATOR_DESC_head():
    class DML_TOP_K_OPERATOR_DESC(Structure):
        pass
    return DML_TOP_K_OPERATOR_DESC
def _define_DML_TOP_K_OPERATOR_DESC():
    DML_TOP_K_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_TOP_K_OPERATOR_DESC_head
    DML_TOP_K_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputValueTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputIndexTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Axis', UInt32),
        ('K', UInt32),
    ]
    return DML_TOP_K_OPERATOR_DESC
def _define_DML_TOP_K1_OPERATOR_DESC_head():
    class DML_TOP_K1_OPERATOR_DESC(Structure):
        pass
    return DML_TOP_K1_OPERATOR_DESC
def _define_DML_TOP_K1_OPERATOR_DESC():
    DML_TOP_K1_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_TOP_K1_OPERATOR_DESC_head
    DML_TOP_K1_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputValueTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputIndexTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Axis', UInt32),
        ('K', UInt32),
        ('AxisDirection', win32more.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION),
    ]
    return DML_TOP_K1_OPERATOR_DESC
def _define_DML_UPSAMPLE_2D_OPERATOR_DESC_head():
    class DML_UPSAMPLE_2D_OPERATOR_DESC(Structure):
        pass
    return DML_UPSAMPLE_2D_OPERATOR_DESC
def _define_DML_UPSAMPLE_2D_OPERATOR_DESC():
    DML_UPSAMPLE_2D_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_UPSAMPLE_2D_OPERATOR_DESC_head
    DML_UPSAMPLE_2D_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('ScaleSize', win32more.AI.MachineLearning.DirectML.DML_SIZE_2D),
        ('InterpolationMode', win32more.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE),
    ]
    return DML_UPSAMPLE_2D_OPERATOR_DESC
def _define_DML_VALUE_SCALE_2D_OPERATOR_DESC_head():
    class DML_VALUE_SCALE_2D_OPERATOR_DESC(Structure):
        pass
    return DML_VALUE_SCALE_2D_OPERATOR_DESC
def _define_DML_VALUE_SCALE_2D_OPERATOR_DESC():
    DML_VALUE_SCALE_2D_OPERATOR_DESC = win32more.AI.MachineLearning.DirectML.DML_VALUE_SCALE_2D_OPERATOR_DESC_head
    DML_VALUE_SCALE_2D_OPERATOR_DESC._fields_ = [
        ('InputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('OutputTensor', POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)),
        ('Scale', Single),
        ('ChannelCount', UInt32),
        ('Bias', POINTER(Single)),
    ]
    return DML_VALUE_SCALE_2D_OPERATOR_DESC
def _define_IDMLBindingTable_head():
    class IDMLBindingTable(win32more.AI.MachineLearning.DirectML.IDMLDeviceChild_head):
        Guid = Guid('29c687dc-de74-4e3b-ab-00-11-68-f2-fc-3c-fc')
    return IDMLBindingTable
def _define_IDMLBindingTable():
    IDMLBindingTable = win32more.AI.MachineLearning.DirectML.IDMLBindingTable_head
    IDMLBindingTable.BindInputs = COMMETHOD(WINFUNCTYPE(Void,UInt32,POINTER(win32more.AI.MachineLearning.DirectML.DML_BINDING_DESC_head))(8, 'BindInputs', ((1, 'bindingCount'),(1, 'bindings'),)))
    IDMLBindingTable.BindOutputs = COMMETHOD(WINFUNCTYPE(Void,UInt32,POINTER(win32more.AI.MachineLearning.DirectML.DML_BINDING_DESC_head))(9, 'BindOutputs', ((1, 'bindingCount'),(1, 'bindings'),)))
    IDMLBindingTable.BindTemporaryResource = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.AI.MachineLearning.DirectML.DML_BINDING_DESC_head))(10, 'BindTemporaryResource', ((1, 'binding'),)))
    IDMLBindingTable.BindPersistentResource = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.AI.MachineLearning.DirectML.DML_BINDING_DESC_head))(11, 'BindPersistentResource', ((1, 'binding'),)))
    IDMLBindingTable.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.AI.MachineLearning.DirectML.DML_BINDING_TABLE_DESC_head))(12, 'Reset', ((1, 'desc'),)))
    win32more.AI.MachineLearning.DirectML.IDMLDeviceChild
    return IDMLBindingTable
def _define_IDMLCommandRecorder_head():
    class IDMLCommandRecorder(win32more.AI.MachineLearning.DirectML.IDMLDeviceChild_head):
        Guid = Guid('e6857a76-2e3e-4fdd-bf-f4-5d-2b-a1-0f-b4-53')
    return IDMLCommandRecorder
def _define_IDMLCommandRecorder():
    IDMLCommandRecorder = win32more.AI.MachineLearning.DirectML.IDMLCommandRecorder_head
    IDMLCommandRecorder.RecordDispatch = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D12.ID3D12CommandList_head,win32more.AI.MachineLearning.DirectML.IDMLDispatchable_head,win32more.AI.MachineLearning.DirectML.IDMLBindingTable_head)(8, 'RecordDispatch', ((1, 'commandList'),(1, 'dispatchable'),(1, 'bindings'),)))
    win32more.AI.MachineLearning.DirectML.IDMLDeviceChild
    return IDMLCommandRecorder
def _define_IDMLCompiledOperator_head():
    class IDMLCompiledOperator(win32more.AI.MachineLearning.DirectML.IDMLDispatchable_head):
        Guid = Guid('6b15e56a-bf5c-4902-92-d8-da-3a-65-0a-fe-a4')
    return IDMLCompiledOperator
def _define_IDMLCompiledOperator():
    IDMLCompiledOperator = win32more.AI.MachineLearning.DirectML.IDMLCompiledOperator_head
    win32more.AI.MachineLearning.DirectML.IDMLDispatchable
    return IDMLCompiledOperator
def _define_IDMLDebugDevice_head():
    class IDMLDebugDevice(win32more.System.Com.IUnknown_head):
        Guid = Guid('7d6f3ac9-394a-4ac3-92-a7-39-0c-c5-7a-82-17')
    return IDMLDebugDevice
def _define_IDMLDebugDevice():
    IDMLDebugDevice = win32more.AI.MachineLearning.DirectML.IDMLDebugDevice_head
    IDMLDebugDevice.SetMuteDebugOutput = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.BOOL)(3, 'SetMuteDebugOutput', ((1, 'mute'),)))
    win32more.System.Com.IUnknown
    return IDMLDebugDevice
def _define_IDMLDevice_head():
    class IDMLDevice(win32more.AI.MachineLearning.DirectML.IDMLObject_head):
        Guid = Guid('6dbd6437-96fd-423f-a9-8c-ae-5e-7c-2a-57-3f')
    return IDMLDevice
def _define_IDMLDevice():
    IDMLDevice = win32more.AI.MachineLearning.DirectML.IDMLDevice_head
    IDMLDevice.CheckFeatureSupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.AI.MachineLearning.DirectML.DML_FEATURE,UInt32,c_void_p,UInt32,c_void_p)(7, 'CheckFeatureSupport', ((1, 'feature'),(1, 'featureQueryDataSize'),(1, 'featureQueryData'),(1, 'featureSupportDataSize'),(1, 'featureSupportData'),)))
    IDMLDevice.CreateOperator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head),POINTER(Guid),POINTER(c_void_p))(8, 'CreateOperator', ((1, 'desc'),(1, 'riid'),(1, 'ppv'),)))
    IDMLDevice.CompileOperator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.AI.MachineLearning.DirectML.IDMLOperator_head,win32more.AI.MachineLearning.DirectML.DML_EXECUTION_FLAGS,POINTER(Guid),POINTER(c_void_p))(9, 'CompileOperator', ((1, 'op'),(1, 'flags'),(1, 'riid'),(1, 'ppv'),)))
    IDMLDevice.CreateOperatorInitializer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.AI.MachineLearning.DirectML.IDMLCompiledOperator_head),POINTER(Guid),POINTER(c_void_p))(10, 'CreateOperatorInitializer', ((1, 'operatorCount'),(1, 'operators'),(1, 'riid'),(1, 'ppv'),)))
    IDMLDevice.CreateCommandRecorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(11, 'CreateCommandRecorder', ((1, 'riid'),(1, 'ppv'),)))
    IDMLDevice.CreateBindingTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.AI.MachineLearning.DirectML.DML_BINDING_TABLE_DESC_head),POINTER(Guid),POINTER(c_void_p))(12, 'CreateBindingTable', ((1, 'desc'),(1, 'riid'),(1, 'ppv'),)))
    IDMLDevice.Evict = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.AI.MachineLearning.DirectML.IDMLPageable_head))(13, 'Evict', ((1, 'count'),(1, 'ppObjects'),)))
    IDMLDevice.MakeResident = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.AI.MachineLearning.DirectML.IDMLPageable_head))(14, 'MakeResident', ((1, 'count'),(1, 'ppObjects'),)))
    IDMLDevice.GetDeviceRemovedReason = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(15, 'GetDeviceRemovedReason', ()))
    IDMLDevice.GetParentDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(16, 'GetParentDevice', ((1, 'riid'),(1, 'ppv'),)))
    win32more.AI.MachineLearning.DirectML.IDMLObject
    return IDMLDevice
def _define_IDMLDevice1_head():
    class IDMLDevice1(win32more.AI.MachineLearning.DirectML.IDMLDevice_head):
        Guid = Guid('a0884f9a-d2be-4355-aa-5d-59-01-28-1a-d1-d2')
    return IDMLDevice1
def _define_IDMLDevice1():
    IDMLDevice1 = win32more.AI.MachineLearning.DirectML.IDMLDevice1_head
    IDMLDevice1.CompileGraph = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.AI.MachineLearning.DirectML.DML_GRAPH_DESC_head),win32more.AI.MachineLearning.DirectML.DML_EXECUTION_FLAGS,POINTER(Guid),POINTER(c_void_p))(17, 'CompileGraph', ((1, 'desc'),(1, 'flags'),(1, 'riid'),(1, 'ppv'),)))
    win32more.AI.MachineLearning.DirectML.IDMLDevice
    return IDMLDevice1
def _define_IDMLDeviceChild_head():
    class IDMLDeviceChild(win32more.AI.MachineLearning.DirectML.IDMLObject_head):
        Guid = Guid('27e83142-8165-49e3-97-4e-2f-d6-6e-4c-b6-9d')
    return IDMLDeviceChild
def _define_IDMLDeviceChild():
    IDMLDeviceChild = win32more.AI.MachineLearning.DirectML.IDMLDeviceChild_head
    IDMLDeviceChild.GetDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(7, 'GetDevice', ((1, 'riid'),(1, 'ppv'),)))
    win32more.AI.MachineLearning.DirectML.IDMLObject
    return IDMLDeviceChild
def _define_IDMLDispatchable_head():
    class IDMLDispatchable(win32more.AI.MachineLearning.DirectML.IDMLPageable_head):
        Guid = Guid('dcb821a8-1039-441e-9f-1c-b1-75-9c-2f-3c-ec')
    return IDMLDispatchable
def _define_IDMLDispatchable():
    IDMLDispatchable = win32more.AI.MachineLearning.DirectML.IDMLDispatchable_head
    IDMLDispatchable.GetBindingProperties = COMMETHOD(WINFUNCTYPE(win32more.AI.MachineLearning.DirectML.DML_BINDING_PROPERTIES,)(8, 'GetBindingProperties', ()))
    win32more.AI.MachineLearning.DirectML.IDMLPageable
    return IDMLDispatchable
def _define_IDMLObject_head():
    class IDMLObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('c8263aac-9e0c-4a2d-9b-8e-00-75-21-a3-31-7c')
    return IDMLObject
def _define_IDMLObject():
    IDMLObject = win32more.AI.MachineLearning.DirectML.IDMLObject_head
    IDMLObject.GetPrivateData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32),c_void_p)(3, 'GetPrivateData', ((1, 'guid'),(1, 'dataSize'),(1, 'data'),)))
    IDMLObject.SetPrivateData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,c_void_p)(4, 'SetPrivateData', ((1, 'guid'),(1, 'dataSize'),(1, 'data'),)))
    IDMLObject.SetPrivateDataInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head)(5, 'SetPrivateDataInterface', ((1, 'guid'),(1, 'data'),)))
    IDMLObject.SetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(6, 'SetName', ((1, 'name'),)))
    win32more.System.Com.IUnknown
    return IDMLObject
def _define_IDMLOperator_head():
    class IDMLOperator(win32more.AI.MachineLearning.DirectML.IDMLDeviceChild_head):
        Guid = Guid('26caae7a-3081-4633-95-81-22-6f-be-57-69-5d')
    return IDMLOperator
def _define_IDMLOperator():
    IDMLOperator = win32more.AI.MachineLearning.DirectML.IDMLOperator_head
    win32more.AI.MachineLearning.DirectML.IDMLDeviceChild
    return IDMLOperator
def _define_IDMLOperatorInitializer_head():
    class IDMLOperatorInitializer(win32more.AI.MachineLearning.DirectML.IDMLDispatchable_head):
        Guid = Guid('427c1113-435c-469c-86-76-4d-5d-d0-72-f8-13')
    return IDMLOperatorInitializer
def _define_IDMLOperatorInitializer():
    IDMLOperatorInitializer = win32more.AI.MachineLearning.DirectML.IDMLOperatorInitializer_head
    IDMLOperatorInitializer.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.AI.MachineLearning.DirectML.IDMLCompiledOperator_head))(9, 'Reset', ((1, 'operatorCount'),(1, 'operators'),)))
    win32more.AI.MachineLearning.DirectML.IDMLDispatchable
    return IDMLOperatorInitializer
def _define_IDMLPageable_head():
    class IDMLPageable(win32more.AI.MachineLearning.DirectML.IDMLDeviceChild_head):
        Guid = Guid('b1ab0825-4542-4a4b-86-17-6d-de-6e-8f-62-01')
    return IDMLPageable
def _define_IDMLPageable():
    IDMLPageable = win32more.AI.MachineLearning.DirectML.IDMLPageable_head
    win32more.AI.MachineLearning.DirectML.IDMLDeviceChild
    return IDMLPageable
__all__ = [
    "DMLCreateDevice",
    "DMLCreateDevice1",
    "DML_ACTIVATION_CELU_OPERATOR_DESC",
    "DML_ACTIVATION_ELU_OPERATOR_DESC",
    "DML_ACTIVATION_HARDMAX_OPERATOR_DESC",
    "DML_ACTIVATION_HARD_SIGMOID_OPERATOR_DESC",
    "DML_ACTIVATION_IDENTITY_OPERATOR_DESC",
    "DML_ACTIVATION_LEAKY_RELU_OPERATOR_DESC",
    "DML_ACTIVATION_LINEAR_OPERATOR_DESC",
    "DML_ACTIVATION_LOG_SOFTMAX_OPERATOR_DESC",
    "DML_ACTIVATION_PARAMETERIZED_RELU_OPERATOR_DESC",
    "DML_ACTIVATION_PARAMETRIC_SOFTPLUS_OPERATOR_DESC",
    "DML_ACTIVATION_RELU_GRAD_OPERATOR_DESC",
    "DML_ACTIVATION_RELU_OPERATOR_DESC",
    "DML_ACTIVATION_SCALED_ELU_OPERATOR_DESC",
    "DML_ACTIVATION_SCALED_TANH_OPERATOR_DESC",
    "DML_ACTIVATION_SHRINK_OPERATOR_DESC",
    "DML_ACTIVATION_SIGMOID_OPERATOR_DESC",
    "DML_ACTIVATION_SOFTMAX_OPERATOR_DESC",
    "DML_ACTIVATION_SOFTPLUS_OPERATOR_DESC",
    "DML_ACTIVATION_SOFTSIGN_OPERATOR_DESC",
    "DML_ACTIVATION_TANH_OPERATOR_DESC",
    "DML_ACTIVATION_THRESHOLDED_RELU_OPERATOR_DESC",
    "DML_ADAM_OPTIMIZER_OPERATOR_DESC",
    "DML_ARGMAX_OPERATOR_DESC",
    "DML_ARGMIN_OPERATOR_DESC",
    "DML_AVERAGE_POOLING_GRAD_OPERATOR_DESC",
    "DML_AVERAGE_POOLING_OPERATOR_DESC",
    "DML_AXIS_DIRECTION",
    "DML_AXIS_DIRECTION_DECREASING",
    "DML_AXIS_DIRECTION_INCREASING",
    "DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC",
    "DML_BATCH_NORMALIZATION_OPERATOR_DESC",
    "DML_BINDING_DESC",
    "DML_BINDING_PROPERTIES",
    "DML_BINDING_TABLE_DESC",
    "DML_BINDING_TYPE",
    "DML_BINDING_TYPE_BUFFER",
    "DML_BINDING_TYPE_BUFFER_ARRAY",
    "DML_BINDING_TYPE_NONE",
    "DML_BUFFER_ARRAY_BINDING",
    "DML_BUFFER_BINDING",
    "DML_BUFFER_TENSOR_DESC",
    "DML_CAST_OPERATOR_DESC",
    "DML_CONVOLUTION_DIRECTION",
    "DML_CONVOLUTION_DIRECTION_BACKWARD",
    "DML_CONVOLUTION_DIRECTION_FORWARD",
    "DML_CONVOLUTION_INTEGER_OPERATOR_DESC",
    "DML_CONVOLUTION_MODE",
    "DML_CONVOLUTION_MODE_CONVOLUTION",
    "DML_CONVOLUTION_MODE_CROSS_CORRELATION",
    "DML_CONVOLUTION_OPERATOR_DESC",
    "DML_CREATE_DEVICE_FLAGS",
    "DML_CREATE_DEVICE_FLAG_DEBUG",
    "DML_CREATE_DEVICE_FLAG_NONE",
    "DML_CUMULATIVE_PRODUCT_OPERATOR_DESC",
    "DML_CUMULATIVE_SUMMATION_OPERATOR_DESC",
    "DML_DEPTH_SPACE_ORDER",
    "DML_DEPTH_SPACE_ORDER_COLUMN_ROW_DEPTH",
    "DML_DEPTH_SPACE_ORDER_DEPTH_COLUMN_ROW",
    "DML_DEPTH_TO_SPACE1_OPERATOR_DESC",
    "DML_DEPTH_TO_SPACE_OPERATOR_DESC",
    "DML_DIAGONAL_MATRIX_OPERATOR_DESC",
    "DML_DYNAMIC_QUANTIZE_LINEAR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ABS_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ACOSH_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ACOS_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ADD1_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ADD_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ASINH_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ASIN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ATANH_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ATAN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ATAN_YX_OPERATOR_DESC",
    "DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC",
    "DML_ELEMENT_WISE_BIT_COUNT_OPERATOR_DESC",
    "DML_ELEMENT_WISE_BIT_NOT_OPERATOR_DESC",
    "DML_ELEMENT_WISE_BIT_OR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_BIT_SHIFT_LEFT_OPERATOR_DESC",
    "DML_ELEMENT_WISE_BIT_SHIFT_RIGHT_OPERATOR_DESC",
    "DML_ELEMENT_WISE_BIT_XOR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_CEIL_OPERATOR_DESC",
    "DML_ELEMENT_WISE_CLIP_GRAD_OPERATOR_DESC",
    "DML_ELEMENT_WISE_CLIP_OPERATOR_DESC",
    "DML_ELEMENT_WISE_CONSTANT_POW_OPERATOR_DESC",
    "DML_ELEMENT_WISE_COSH_OPERATOR_DESC",
    "DML_ELEMENT_WISE_COS_OPERATOR_DESC",
    "DML_ELEMENT_WISE_DEQUANTIZE_LINEAR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_DIFFERENCE_SQUARE_OPERATOR_DESC",
    "DML_ELEMENT_WISE_DIVIDE_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ERF_OPERATOR_DESC",
    "DML_ELEMENT_WISE_EXP_OPERATOR_DESC",
    "DML_ELEMENT_WISE_FLOOR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_IDENTITY_OPERATOR_DESC",
    "DML_ELEMENT_WISE_IF_OPERATOR_DESC",
    "DML_ELEMENT_WISE_IS_INFINITY_OPERATOR_DESC",
    "DML_ELEMENT_WISE_IS_NAN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_AND_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_EQUALS_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_NOT_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_OR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_XOR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOG_OPERATOR_DESC",
    "DML_ELEMENT_WISE_MAX_OPERATOR_DESC",
    "DML_ELEMENT_WISE_MEAN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_MIN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_MODULUS_FLOOR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_MODULUS_TRUNCATE_OPERATOR_DESC",
    "DML_ELEMENT_WISE_MULTIPLY_OPERATOR_DESC",
    "DML_ELEMENT_WISE_POW_OPERATOR_DESC",
    "DML_ELEMENT_WISE_QUANTIZED_LINEAR_ADD_OPERATOR_DESC",
    "DML_ELEMENT_WISE_QUANTIZE_LINEAR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_RECIP_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ROUND_OPERATOR_DESC",
    "DML_ELEMENT_WISE_SIGN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_SINH_OPERATOR_DESC",
    "DML_ELEMENT_WISE_SIN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_SQRT_OPERATOR_DESC",
    "DML_ELEMENT_WISE_SUBTRACT_OPERATOR_DESC",
    "DML_ELEMENT_WISE_TANH_OPERATOR_DESC",
    "DML_ELEMENT_WISE_TAN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_THRESHOLD_OPERATOR_DESC",
    "DML_EXECUTION_FLAGS",
    "DML_EXECUTION_FLAG_ALLOW_HALF_PRECISION_COMPUTATION",
    "DML_EXECUTION_FLAG_DESCRIPTORS_VOLATILE",
    "DML_EXECUTION_FLAG_DISABLE_META_COMMANDS",
    "DML_EXECUTION_FLAG_NONE",
    "DML_FEATURE",
    "DML_FEATURE_DATA_FEATURE_LEVELS",
    "DML_FEATURE_DATA_TENSOR_DATA_TYPE_SUPPORT",
    "DML_FEATURE_FEATURE_LEVELS",
    "DML_FEATURE_LEVEL",
    "DML_FEATURE_LEVEL_1_0",
    "DML_FEATURE_LEVEL_2_0",
    "DML_FEATURE_LEVEL_2_1",
    "DML_FEATURE_LEVEL_3_0",
    "DML_FEATURE_LEVEL_3_1",
    "DML_FEATURE_LEVEL_4_0",
    "DML_FEATURE_QUERY_FEATURE_LEVELS",
    "DML_FEATURE_QUERY_TENSOR_DATA_TYPE_SUPPORT",
    "DML_FEATURE_TENSOR_DATA_TYPE_SUPPORT",
    "DML_FILL_VALUE_CONSTANT_OPERATOR_DESC",
    "DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC",
    "DML_GATHER_ELEMENTS_OPERATOR_DESC",
    "DML_GATHER_ND1_OPERATOR_DESC",
    "DML_GATHER_ND_OPERATOR_DESC",
    "DML_GATHER_OPERATOR_DESC",
    "DML_GEMM_OPERATOR_DESC",
    "DML_GRAPH_DESC",
    "DML_GRAPH_EDGE_DESC",
    "DML_GRAPH_EDGE_TYPE",
    "DML_GRAPH_EDGE_TYPE_INPUT",
    "DML_GRAPH_EDGE_TYPE_INTERMEDIATE",
    "DML_GRAPH_EDGE_TYPE_INVALID",
    "DML_GRAPH_EDGE_TYPE_OUTPUT",
    "DML_GRAPH_NODE_DESC",
    "DML_GRAPH_NODE_TYPE",
    "DML_GRAPH_NODE_TYPE_INVALID",
    "DML_GRAPH_NODE_TYPE_OPERATOR",
    "DML_GRU_OPERATOR_DESC",
    "DML_INPUT_GRAPH_EDGE_DESC",
    "DML_INTERMEDIATE_GRAPH_EDGE_DESC",
    "DML_INTERPOLATION_MODE",
    "DML_INTERPOLATION_MODE_LINEAR",
    "DML_INTERPOLATION_MODE_NEAREST_NEIGHBOR",
    "DML_IS_INFINITY_MODE",
    "DML_IS_INFINITY_MODE_EITHER",
    "DML_IS_INFINITY_MODE_NEGATIVE",
    "DML_IS_INFINITY_MODE_POSITIVE",
    "DML_JOIN_OPERATOR_DESC",
    "DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC",
    "DML_LOCAL_RESPONSE_NORMALIZATION_OPERATOR_DESC",
    "DML_LP_NORMALIZATION_OPERATOR_DESC",
    "DML_LP_POOLING_OPERATOR_DESC",
    "DML_LSTM_OPERATOR_DESC",
    "DML_MATRIX_MULTIPLY_INTEGER_OPERATOR_DESC",
    "DML_MATRIX_TRANSFORM",
    "DML_MATRIX_TRANSFORM_NONE",
    "DML_MATRIX_TRANSFORM_TRANSPOSE",
    "DML_MAX_POOLING1_OPERATOR_DESC",
    "DML_MAX_POOLING2_OPERATOR_DESC",
    "DML_MAX_POOLING_GRAD_OPERATOR_DESC",
    "DML_MAX_POOLING_OPERATOR_DESC",
    "DML_MAX_UNPOOLING_OPERATOR_DESC",
    "DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC",
    "DML_MEAN_VARIANCE_NORMALIZATION_OPERATOR_DESC",
    "DML_MINIMUM_BUFFER_TENSOR_ALIGNMENT",
    "DML_NONZERO_COORDINATES_OPERATOR_DESC",
    "DML_ONE_HOT_OPERATOR_DESC",
    "DML_OPERATOR_ACTIVATION_CELU",
    "DML_OPERATOR_ACTIVATION_ELU",
    "DML_OPERATOR_ACTIVATION_HARDMAX",
    "DML_OPERATOR_ACTIVATION_HARD_SIGMOID",
    "DML_OPERATOR_ACTIVATION_IDENTITY",
    "DML_OPERATOR_ACTIVATION_LEAKY_RELU",
    "DML_OPERATOR_ACTIVATION_LINEAR",
    "DML_OPERATOR_ACTIVATION_LOG_SOFTMAX",
    "DML_OPERATOR_ACTIVATION_PARAMETERIZED_RELU",
    "DML_OPERATOR_ACTIVATION_PARAMETRIC_SOFTPLUS",
    "DML_OPERATOR_ACTIVATION_RELU",
    "DML_OPERATOR_ACTIVATION_RELU_GRAD",
    "DML_OPERATOR_ACTIVATION_SCALED_ELU",
    "DML_OPERATOR_ACTIVATION_SCALED_TANH",
    "DML_OPERATOR_ACTIVATION_SHRINK",
    "DML_OPERATOR_ACTIVATION_SIGMOID",
    "DML_OPERATOR_ACTIVATION_SOFTMAX",
    "DML_OPERATOR_ACTIVATION_SOFTPLUS",
    "DML_OPERATOR_ACTIVATION_SOFTSIGN",
    "DML_OPERATOR_ACTIVATION_TANH",
    "DML_OPERATOR_ACTIVATION_THRESHOLDED_RELU",
    "DML_OPERATOR_ADAM_OPTIMIZER",
    "DML_OPERATOR_ARGMAX",
    "DML_OPERATOR_ARGMIN",
    "DML_OPERATOR_AVERAGE_POOLING",
    "DML_OPERATOR_AVERAGE_POOLING_GRAD",
    "DML_OPERATOR_BATCH_NORMALIZATION",
    "DML_OPERATOR_BATCH_NORMALIZATION_GRAD",
    "DML_OPERATOR_CAST",
    "DML_OPERATOR_CONVOLUTION",
    "DML_OPERATOR_CONVOLUTION_INTEGER",
    "DML_OPERATOR_CUMULATIVE_PRODUCT",
    "DML_OPERATOR_CUMULATIVE_SUMMATION",
    "DML_OPERATOR_DEPTH_TO_SPACE",
    "DML_OPERATOR_DEPTH_TO_SPACE1",
    "DML_OPERATOR_DESC",
    "DML_OPERATOR_DIAGONAL_MATRIX",
    "DML_OPERATOR_DYNAMIC_QUANTIZE_LINEAR",
    "DML_OPERATOR_ELEMENT_WISE_ABS",
    "DML_OPERATOR_ELEMENT_WISE_ACOS",
    "DML_OPERATOR_ELEMENT_WISE_ACOSH",
    "DML_OPERATOR_ELEMENT_WISE_ADD",
    "DML_OPERATOR_ELEMENT_WISE_ADD1",
    "DML_OPERATOR_ELEMENT_WISE_ASIN",
    "DML_OPERATOR_ELEMENT_WISE_ASINH",
    "DML_OPERATOR_ELEMENT_WISE_ATAN",
    "DML_OPERATOR_ELEMENT_WISE_ATANH",
    "DML_OPERATOR_ELEMENT_WISE_ATAN_YX",
    "DML_OPERATOR_ELEMENT_WISE_BIT_AND",
    "DML_OPERATOR_ELEMENT_WISE_BIT_COUNT",
    "DML_OPERATOR_ELEMENT_WISE_BIT_NOT",
    "DML_OPERATOR_ELEMENT_WISE_BIT_OR",
    "DML_OPERATOR_ELEMENT_WISE_BIT_SHIFT_LEFT",
    "DML_OPERATOR_ELEMENT_WISE_BIT_SHIFT_RIGHT",
    "DML_OPERATOR_ELEMENT_WISE_BIT_XOR",
    "DML_OPERATOR_ELEMENT_WISE_CEIL",
    "DML_OPERATOR_ELEMENT_WISE_CLIP",
    "DML_OPERATOR_ELEMENT_WISE_CLIP_GRAD",
    "DML_OPERATOR_ELEMENT_WISE_CONSTANT_POW",
    "DML_OPERATOR_ELEMENT_WISE_COS",
    "DML_OPERATOR_ELEMENT_WISE_COSH",
    "DML_OPERATOR_ELEMENT_WISE_DEQUANTIZE_LINEAR",
    "DML_OPERATOR_ELEMENT_WISE_DIFFERENCE_SQUARE",
    "DML_OPERATOR_ELEMENT_WISE_DIVIDE",
    "DML_OPERATOR_ELEMENT_WISE_ERF",
    "DML_OPERATOR_ELEMENT_WISE_EXP",
    "DML_OPERATOR_ELEMENT_WISE_FLOOR",
    "DML_OPERATOR_ELEMENT_WISE_IDENTITY",
    "DML_OPERATOR_ELEMENT_WISE_IF",
    "DML_OPERATOR_ELEMENT_WISE_IS_INFINITY",
    "DML_OPERATOR_ELEMENT_WISE_IS_NAN",
    "DML_OPERATOR_ELEMENT_WISE_LOG",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_AND",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_EQUALS",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_GREATER_THAN",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_LESS_THAN",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_NOT",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_OR",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_XOR",
    "DML_OPERATOR_ELEMENT_WISE_MAX",
    "DML_OPERATOR_ELEMENT_WISE_MEAN",
    "DML_OPERATOR_ELEMENT_WISE_MIN",
    "DML_OPERATOR_ELEMENT_WISE_MODULUS_FLOOR",
    "DML_OPERATOR_ELEMENT_WISE_MODULUS_TRUNCATE",
    "DML_OPERATOR_ELEMENT_WISE_MULTIPLY",
    "DML_OPERATOR_ELEMENT_WISE_POW",
    "DML_OPERATOR_ELEMENT_WISE_QUANTIZED_LINEAR_ADD",
    "DML_OPERATOR_ELEMENT_WISE_QUANTIZE_LINEAR",
    "DML_OPERATOR_ELEMENT_WISE_RECIP",
    "DML_OPERATOR_ELEMENT_WISE_ROUND",
    "DML_OPERATOR_ELEMENT_WISE_SIGN",
    "DML_OPERATOR_ELEMENT_WISE_SIN",
    "DML_OPERATOR_ELEMENT_WISE_SINH",
    "DML_OPERATOR_ELEMENT_WISE_SQRT",
    "DML_OPERATOR_ELEMENT_WISE_SUBTRACT",
    "DML_OPERATOR_ELEMENT_WISE_TAN",
    "DML_OPERATOR_ELEMENT_WISE_TANH",
    "DML_OPERATOR_ELEMENT_WISE_THRESHOLD",
    "DML_OPERATOR_FILL_VALUE_CONSTANT",
    "DML_OPERATOR_FILL_VALUE_SEQUENCE",
    "DML_OPERATOR_GATHER",
    "DML_OPERATOR_GATHER_ELEMENTS",
    "DML_OPERATOR_GATHER_ND",
    "DML_OPERATOR_GATHER_ND1",
    "DML_OPERATOR_GEMM",
    "DML_OPERATOR_GRAPH_NODE_DESC",
    "DML_OPERATOR_GRU",
    "DML_OPERATOR_INVALID",
    "DML_OPERATOR_JOIN",
    "DML_OPERATOR_LOCAL_RESPONSE_NORMALIZATION",
    "DML_OPERATOR_LOCAL_RESPONSE_NORMALIZATION_GRAD",
    "DML_OPERATOR_LP_NORMALIZATION",
    "DML_OPERATOR_LP_POOLING",
    "DML_OPERATOR_LSTM",
    "DML_OPERATOR_MATRIX_MULTIPLY_INTEGER",
    "DML_OPERATOR_MAX_POOLING",
    "DML_OPERATOR_MAX_POOLING1",
    "DML_OPERATOR_MAX_POOLING2",
    "DML_OPERATOR_MAX_POOLING_GRAD",
    "DML_OPERATOR_MAX_UNPOOLING",
    "DML_OPERATOR_MEAN_VARIANCE_NORMALIZATION",
    "DML_OPERATOR_MEAN_VARIANCE_NORMALIZATION1",
    "DML_OPERATOR_NONZERO_COORDINATES",
    "DML_OPERATOR_ONE_HOT",
    "DML_OPERATOR_PADDING",
    "DML_OPERATOR_QUANTIZED_LINEAR_CONVOLUTION",
    "DML_OPERATOR_QUANTIZED_LINEAR_MATRIX_MULTIPLY",
    "DML_OPERATOR_RANDOM_GENERATOR",
    "DML_OPERATOR_REDUCE",
    "DML_OPERATOR_RESAMPLE",
    "DML_OPERATOR_RESAMPLE1",
    "DML_OPERATOR_RESAMPLE_GRAD",
    "DML_OPERATOR_REVERSE_SUBSEQUENCES",
    "DML_OPERATOR_RNN",
    "DML_OPERATOR_ROI_ALIGN",
    "DML_OPERATOR_ROI_ALIGN1",
    "DML_OPERATOR_ROI_POOLING",
    "DML_OPERATOR_SCATTER",
    "DML_OPERATOR_SCATTER_ELEMENTS",
    "DML_OPERATOR_SCATTER_ND",
    "DML_OPERATOR_SLICE",
    "DML_OPERATOR_SLICE1",
    "DML_OPERATOR_SLICE_GRAD",
    "DML_OPERATOR_SPACE_TO_DEPTH",
    "DML_OPERATOR_SPACE_TO_DEPTH1",
    "DML_OPERATOR_SPLIT",
    "DML_OPERATOR_TILE",
    "DML_OPERATOR_TOP_K",
    "DML_OPERATOR_TOP_K1",
    "DML_OPERATOR_TYPE",
    "DML_OPERATOR_UPSAMPLE_2D",
    "DML_OPERATOR_VALUE_SCALE_2D",
    "DML_OUTPUT_GRAPH_EDGE_DESC",
    "DML_PADDING_MODE",
    "DML_PADDING_MODE_CONSTANT",
    "DML_PADDING_MODE_EDGE",
    "DML_PADDING_MODE_REFLECTION",
    "DML_PADDING_MODE_SYMMETRIC",
    "DML_PADDING_OPERATOR_DESC",
    "DML_PERSISTENT_BUFFER_ALIGNMENT",
    "DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC",
    "DML_QUANTIZED_LINEAR_MATRIX_MULTIPLY_OPERATOR_DESC",
    "DML_RANDOM_GENERATOR_OPERATOR_DESC",
    "DML_RANDOM_GENERATOR_TYPE",
    "DML_RANDOM_GENERATOR_TYPE_PHILOX_4X32_10",
    "DML_RECURRENT_NETWORK_DIRECTION",
    "DML_RECURRENT_NETWORK_DIRECTION_BACKWARD",
    "DML_RECURRENT_NETWORK_DIRECTION_BIDIRECTIONAL",
    "DML_RECURRENT_NETWORK_DIRECTION_FORWARD",
    "DML_REDUCE_FUNCTION",
    "DML_REDUCE_FUNCTION_ARGMAX",
    "DML_REDUCE_FUNCTION_ARGMIN",
    "DML_REDUCE_FUNCTION_AVERAGE",
    "DML_REDUCE_FUNCTION_L1",
    "DML_REDUCE_FUNCTION_L2",
    "DML_REDUCE_FUNCTION_LOG_SUM",
    "DML_REDUCE_FUNCTION_LOG_SUM_EXP",
    "DML_REDUCE_FUNCTION_MAX",
    "DML_REDUCE_FUNCTION_MIN",
    "DML_REDUCE_FUNCTION_MULTIPLY",
    "DML_REDUCE_FUNCTION_SUM",
    "DML_REDUCE_FUNCTION_SUM_SQUARE",
    "DML_REDUCE_OPERATOR_DESC",
    "DML_RESAMPLE1_OPERATOR_DESC",
    "DML_RESAMPLE_GRAD_OPERATOR_DESC",
    "DML_RESAMPLE_OPERATOR_DESC",
    "DML_REVERSE_SUBSEQUENCES_OPERATOR_DESC",
    "DML_RNN_OPERATOR_DESC",
    "DML_ROI_ALIGN1_OPERATOR_DESC",
    "DML_ROI_ALIGN_OPERATOR_DESC",
    "DML_ROI_POOLING_OPERATOR_DESC",
    "DML_ROUNDING_MODE",
    "DML_ROUNDING_MODE_HALVES_TO_NEAREST_EVEN",
    "DML_ROUNDING_MODE_TOWARD_INFINITY",
    "DML_ROUNDING_MODE_TOWARD_ZERO",
    "DML_SCALAR_UNION",
    "DML_SCALE_BIAS",
    "DML_SCATTER_ND_OPERATOR_DESC",
    "DML_SCATTER_OPERATOR_DESC",
    "DML_SIZE_2D",
    "DML_SLICE1_OPERATOR_DESC",
    "DML_SLICE_GRAD_OPERATOR_DESC",
    "DML_SLICE_OPERATOR_DESC",
    "DML_SPACE_TO_DEPTH1_OPERATOR_DESC",
    "DML_SPACE_TO_DEPTH_OPERATOR_DESC",
    "DML_SPLIT_OPERATOR_DESC",
    "DML_TARGET_VERSION",
    "DML_TEMPORARY_BUFFER_ALIGNMENT",
    "DML_TENSOR_DATA_TYPE",
    "DML_TENSOR_DATA_TYPE_FLOAT16",
    "DML_TENSOR_DATA_TYPE_FLOAT32",
    "DML_TENSOR_DATA_TYPE_FLOAT64",
    "DML_TENSOR_DATA_TYPE_INT16",
    "DML_TENSOR_DATA_TYPE_INT32",
    "DML_TENSOR_DATA_TYPE_INT64",
    "DML_TENSOR_DATA_TYPE_INT8",
    "DML_TENSOR_DATA_TYPE_UINT16",
    "DML_TENSOR_DATA_TYPE_UINT32",
    "DML_TENSOR_DATA_TYPE_UINT64",
    "DML_TENSOR_DATA_TYPE_UINT8",
    "DML_TENSOR_DATA_TYPE_UNKNOWN",
    "DML_TENSOR_DESC",
    "DML_TENSOR_DIMENSION_COUNT_MAX",
    "DML_TENSOR_DIMENSION_COUNT_MAX1",
    "DML_TENSOR_FLAGS",
    "DML_TENSOR_FLAG_NONE",
    "DML_TENSOR_FLAG_OWNED_BY_DML",
    "DML_TENSOR_TYPE",
    "DML_TENSOR_TYPE_BUFFER",
    "DML_TENSOR_TYPE_INVALID",
    "DML_TILE_OPERATOR_DESC",
    "DML_TOP_K1_OPERATOR_DESC",
    "DML_TOP_K_OPERATOR_DESC",
    "DML_UPSAMPLE_2D_OPERATOR_DESC",
    "DML_VALUE_SCALE_2D_OPERATOR_DESC",
    "IDMLBindingTable",
    "IDMLCommandRecorder",
    "IDMLCompiledOperator",
    "IDMLDebugDevice",
    "IDMLDevice",
    "IDMLDevice1",
    "IDMLDeviceChild",
    "IDMLDispatchable",
    "IDMLObject",
    "IDMLOperator",
    "IDMLOperatorInitializer",
    "IDMLPageable",
]
