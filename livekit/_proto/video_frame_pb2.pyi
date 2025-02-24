"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2023 LiveKit, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
from . import handle_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _VideoCodec:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _VideoCodecEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VideoCodec.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    VP8: _VideoCodec.ValueType  # 0
    H264: _VideoCodec.ValueType  # 1
    AV1: _VideoCodec.ValueType  # 2

class VideoCodec(_VideoCodec, metaclass=_VideoCodecEnumTypeWrapper): ...

VP8: VideoCodec.ValueType  # 0
H264: VideoCodec.ValueType  # 1
AV1: VideoCodec.ValueType  # 2
global___VideoCodec = VideoCodec

class _VideoRotation:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _VideoRotationEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VideoRotation.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    VIDEO_ROTATION_0: _VideoRotation.ValueType  # 0
    VIDEO_ROTATION_90: _VideoRotation.ValueType  # 1
    VIDEO_ROTATION_180: _VideoRotation.ValueType  # 2
    VIDEO_ROTATION_270: _VideoRotation.ValueType  # 3

class VideoRotation(_VideoRotation, metaclass=_VideoRotationEnumTypeWrapper): ...

VIDEO_ROTATION_0: VideoRotation.ValueType  # 0
VIDEO_ROTATION_90: VideoRotation.ValueType  # 1
VIDEO_ROTATION_180: VideoRotation.ValueType  # 2
VIDEO_ROTATION_270: VideoRotation.ValueType  # 3
global___VideoRotation = VideoRotation

class _VideoFormatType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _VideoFormatTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VideoFormatType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    FORMAT_ARGB: _VideoFormatType.ValueType  # 0
    FORMAT_BGRA: _VideoFormatType.ValueType  # 1
    FORMAT_ABGR: _VideoFormatType.ValueType  # 2
    FORMAT_RGBA: _VideoFormatType.ValueType  # 3

class VideoFormatType(_VideoFormatType, metaclass=_VideoFormatTypeEnumTypeWrapper): ...

FORMAT_ARGB: VideoFormatType.ValueType  # 0
FORMAT_BGRA: VideoFormatType.ValueType  # 1
FORMAT_ABGR: VideoFormatType.ValueType  # 2
FORMAT_RGBA: VideoFormatType.ValueType  # 3
global___VideoFormatType = VideoFormatType

class _VideoFrameBufferType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _VideoFrameBufferTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VideoFrameBufferType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NATIVE: _VideoFrameBufferType.ValueType  # 0
    I420: _VideoFrameBufferType.ValueType  # 1
    I420A: _VideoFrameBufferType.ValueType  # 2
    I422: _VideoFrameBufferType.ValueType  # 3
    I444: _VideoFrameBufferType.ValueType  # 4
    I010: _VideoFrameBufferType.ValueType  # 5
    NV12: _VideoFrameBufferType.ValueType  # 6

class VideoFrameBufferType(_VideoFrameBufferType, metaclass=_VideoFrameBufferTypeEnumTypeWrapper): ...

NATIVE: VideoFrameBufferType.ValueType  # 0
I420: VideoFrameBufferType.ValueType  # 1
I420A: VideoFrameBufferType.ValueType  # 2
I422: VideoFrameBufferType.ValueType  # 3
I444: VideoFrameBufferType.ValueType  # 4
I010: VideoFrameBufferType.ValueType  # 5
NV12: VideoFrameBufferType.ValueType  # 6
global___VideoFrameBufferType = VideoFrameBufferType

class _VideoStreamType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _VideoStreamTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VideoStreamType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    VIDEO_STREAM_NATIVE: _VideoStreamType.ValueType  # 0
    VIDEO_STREAM_WEBGL: _VideoStreamType.ValueType  # 1
    VIDEO_STREAM_HTML: _VideoStreamType.ValueType  # 2

class VideoStreamType(_VideoStreamType, metaclass=_VideoStreamTypeEnumTypeWrapper):
    """
    VideoStream
    """

VIDEO_STREAM_NATIVE: VideoStreamType.ValueType  # 0
VIDEO_STREAM_WEBGL: VideoStreamType.ValueType  # 1
VIDEO_STREAM_HTML: VideoStreamType.ValueType  # 2
global___VideoStreamType = VideoStreamType

class _VideoSourceType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _VideoSourceTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VideoSourceType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    VIDEO_SOURCE_NATIVE: _VideoSourceType.ValueType  # 0

class VideoSourceType(_VideoSourceType, metaclass=_VideoSourceTypeEnumTypeWrapper): ...

VIDEO_SOURCE_NATIVE: VideoSourceType.ValueType  # 0
global___VideoSourceType = VideoSourceType

@typing_extensions.final
class AllocVideoBufferRequest(google.protobuf.message.Message):
    """Allocate a new VideoFrameBuffer"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    WIDTH_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    type: global___VideoFrameBufferType.ValueType
    """Only I420 is supported atm"""
    width: builtins.int
    height: builtins.int
    def __init__(
        self,
        *,
        type: global___VideoFrameBufferType.ValueType = ...,
        width: builtins.int = ...,
        height: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["height", b"height", "type", b"type", "width", b"width"]) -> None: ...

global___AllocVideoBufferRequest = AllocVideoBufferRequest

@typing_extensions.final
class AllocVideoBufferResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUFFER_FIELD_NUMBER: builtins.int
    @property
    def buffer(self) -> global___OwnedVideoFrameBuffer: ...
    def __init__(
        self,
        *,
        buffer: global___OwnedVideoFrameBuffer | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["buffer", b"buffer"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["buffer", b"buffer"]) -> None: ...

global___AllocVideoBufferResponse = AllocVideoBufferResponse

@typing_extensions.final
class NewVideoStreamRequest(google.protobuf.message.Message):
    """Create a new VideoStream
    VideoStream is used to receive video frames from a track
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRACK_HANDLE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    track_handle: builtins.int
    type: global___VideoStreamType.ValueType
    def __init__(
        self,
        *,
        track_handle: builtins.int = ...,
        type: global___VideoStreamType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["track_handle", b"track_handle", "type", b"type"]) -> None: ...

global___NewVideoStreamRequest = NewVideoStreamRequest

@typing_extensions.final
class NewVideoStreamResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_FIELD_NUMBER: builtins.int
    @property
    def stream(self) -> global___OwnedVideoStream: ...
    def __init__(
        self,
        *,
        stream: global___OwnedVideoStream | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["stream", b"stream"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["stream", b"stream"]) -> None: ...

global___NewVideoStreamResponse = NewVideoStreamResponse

@typing_extensions.final
class NewVideoSourceRequest(google.protobuf.message.Message):
    """Create a new VideoSource
    VideoSource is used to send video frame to a track
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    RESOLUTION_FIELD_NUMBER: builtins.int
    type: global___VideoSourceType.ValueType
    @property
    def resolution(self) -> global___VideoSourceResolution:
        """Used to determine which encodings to use + simulcast layers
        Most of the time it corresponds to the source resolution
        """
    def __init__(
        self,
        *,
        type: global___VideoSourceType.ValueType = ...,
        resolution: global___VideoSourceResolution | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["resolution", b"resolution"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["resolution", b"resolution", "type", b"type"]) -> None: ...

global___NewVideoSourceRequest = NewVideoSourceRequest

@typing_extensions.final
class NewVideoSourceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_FIELD_NUMBER: builtins.int
    @property
    def source(self) -> global___OwnedVideoSource: ...
    def __init__(
        self,
        *,
        source: global___OwnedVideoSource | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["source", b"source"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["source", b"source"]) -> None: ...

global___NewVideoSourceResponse = NewVideoSourceResponse

@typing_extensions.final
class CaptureVideoFrameRequest(google.protobuf.message.Message):
    """Push a frame to a VideoSource"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_HANDLE_FIELD_NUMBER: builtins.int
    FRAME_FIELD_NUMBER: builtins.int
    BUFFER_HANDLE_FIELD_NUMBER: builtins.int
    source_handle: builtins.int
    @property
    def frame(self) -> global___VideoFrameInfo: ...
    buffer_handle: builtins.int
    def __init__(
        self,
        *,
        source_handle: builtins.int = ...,
        frame: global___VideoFrameInfo | None = ...,
        buffer_handle: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["frame", b"frame"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["buffer_handle", b"buffer_handle", "frame", b"frame", "source_handle", b"source_handle"]) -> None: ...

global___CaptureVideoFrameRequest = CaptureVideoFrameRequest

@typing_extensions.final
class CaptureVideoFrameResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___CaptureVideoFrameResponse = CaptureVideoFrameResponse

@typing_extensions.final
class ToI420Request(google.protobuf.message.Message):
    """Convert a RGBA frame to a I420 YUV frame
    Or convert another YUV frame format to I420
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FLIP_Y_FIELD_NUMBER: builtins.int
    ARGB_FIELD_NUMBER: builtins.int
    YUV_HANDLE_FIELD_NUMBER: builtins.int
    flip_y: builtins.bool
    @property
    def argb(self) -> global___ArgbBufferInfo: ...
    yuv_handle: builtins.int
    """Another yuv buffer"""
    def __init__(
        self,
        *,
        flip_y: builtins.bool = ...,
        argb: global___ArgbBufferInfo | None = ...,
        yuv_handle: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["argb", b"argb", "from", b"from", "yuv_handle", b"yuv_handle"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["argb", b"argb", "flip_y", b"flip_y", "from", b"from", "yuv_handle", b"yuv_handle"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["from", b"from"]) -> typing_extensions.Literal["argb", "yuv_handle"] | None: ...

global___ToI420Request = ToI420Request

@typing_extensions.final
class ToI420Response(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUFFER_FIELD_NUMBER: builtins.int
    @property
    def buffer(self) -> global___OwnedVideoFrameBuffer: ...
    def __init__(
        self,
        *,
        buffer: global___OwnedVideoFrameBuffer | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["buffer", b"buffer"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["buffer", b"buffer"]) -> None: ...

global___ToI420Response = ToI420Response

@typing_extensions.final
class ToArgbRequest(google.protobuf.message.Message):
    """Convert a YUV frame to a RGBA frame
    Only I420 is supported atm
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUFFER_HANDLE_FIELD_NUMBER: builtins.int
    DST_PTR_FIELD_NUMBER: builtins.int
    DST_FORMAT_FIELD_NUMBER: builtins.int
    DST_STRIDE_FIELD_NUMBER: builtins.int
    DST_WIDTH_FIELD_NUMBER: builtins.int
    DST_HEIGHT_FIELD_NUMBER: builtins.int
    FLIP_Y_FIELD_NUMBER: builtins.int
    buffer_handle: builtins.int
    dst_ptr: builtins.int
    dst_format: global___VideoFormatType.ValueType
    dst_stride: builtins.int
    dst_width: builtins.int
    dst_height: builtins.int
    flip_y: builtins.bool
    def __init__(
        self,
        *,
        buffer_handle: builtins.int = ...,
        dst_ptr: builtins.int = ...,
        dst_format: global___VideoFormatType.ValueType = ...,
        dst_stride: builtins.int = ...,
        dst_width: builtins.int = ...,
        dst_height: builtins.int = ...,
        flip_y: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["buffer_handle", b"buffer_handle", "dst_format", b"dst_format", "dst_height", b"dst_height", "dst_ptr", b"dst_ptr", "dst_stride", b"dst_stride", "dst_width", b"dst_width", "flip_y", b"flip_y"]) -> None: ...

global___ToArgbRequest = ToArgbRequest

@typing_extensions.final
class ToArgbResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ToArgbResponse = ToArgbResponse

@typing_extensions.final
class VideoResolution(google.protobuf.message.Message):
    """
    VideoFrame buffers
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WIDTH_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    FRAME_RATE_FIELD_NUMBER: builtins.int
    width: builtins.int
    height: builtins.int
    frame_rate: builtins.float
    def __init__(
        self,
        *,
        width: builtins.int = ...,
        height: builtins.int = ...,
        frame_rate: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["frame_rate", b"frame_rate", "height", b"height", "width", b"width"]) -> None: ...

global___VideoResolution = VideoResolution

@typing_extensions.final
class ArgbBufferInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PTR_FIELD_NUMBER: builtins.int
    FORMAT_FIELD_NUMBER: builtins.int
    STRIDE_FIELD_NUMBER: builtins.int
    WIDTH_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    ptr: builtins.int
    format: global___VideoFormatType.ValueType
    stride: builtins.int
    width: builtins.int
    height: builtins.int
    def __init__(
        self,
        *,
        ptr: builtins.int = ...,
        format: global___VideoFormatType.ValueType = ...,
        stride: builtins.int = ...,
        width: builtins.int = ...,
        height: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["format", b"format", "height", b"height", "ptr", b"ptr", "stride", b"stride", "width", b"width"]) -> None: ...

global___ArgbBufferInfo = ArgbBufferInfo

@typing_extensions.final
class VideoFrameInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_US_FIELD_NUMBER: builtins.int
    ROTATION_FIELD_NUMBER: builtins.int
    timestamp_us: builtins.int
    """In microseconds"""
    rotation: global___VideoRotation.ValueType
    def __init__(
        self,
        *,
        timestamp_us: builtins.int = ...,
        rotation: global___VideoRotation.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["rotation", b"rotation", "timestamp_us", b"timestamp_us"]) -> None: ...

global___VideoFrameInfo = VideoFrameInfo

@typing_extensions.final
class VideoFrameBufferInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUFFER_TYPE_FIELD_NUMBER: builtins.int
    WIDTH_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    YUV_FIELD_NUMBER: builtins.int
    BI_YUV_FIELD_NUMBER: builtins.int
    NATIVE_FIELD_NUMBER: builtins.int
    buffer_type: global___VideoFrameBufferType.ValueType
    width: builtins.int
    height: builtins.int
    @property
    def yuv(self) -> global___PlanarYuvBufferInfo: ...
    @property
    def bi_yuv(self) -> global___BiplanarYuvBufferInfo: ...
    @property
    def native(self) -> global___NativeBufferInfo: ...
    def __init__(
        self,
        *,
        buffer_type: global___VideoFrameBufferType.ValueType = ...,
        width: builtins.int = ...,
        height: builtins.int = ...,
        yuv: global___PlanarYuvBufferInfo | None = ...,
        bi_yuv: global___BiplanarYuvBufferInfo | None = ...,
        native: global___NativeBufferInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bi_yuv", b"bi_yuv", "buffer", b"buffer", "native", b"native", "yuv", b"yuv"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bi_yuv", b"bi_yuv", "buffer", b"buffer", "buffer_type", b"buffer_type", "height", b"height", "native", b"native", "width", b"width", "yuv", b"yuv"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["buffer", b"buffer"]) -> typing_extensions.Literal["yuv", "bi_yuv", "native"] | None: ...

global___VideoFrameBufferInfo = VideoFrameBufferInfo

@typing_extensions.final
class OwnedVideoFrameBuffer(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HANDLE_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    @property
    def handle(self) -> handle_pb2.FfiOwnedHandle: ...
    @property
    def info(self) -> global___VideoFrameBufferInfo: ...
    def __init__(
        self,
        *,
        handle: handle_pb2.FfiOwnedHandle | None = ...,
        info: global___VideoFrameBufferInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["handle", b"handle", "info", b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["handle", b"handle", "info", b"info"]) -> None: ...

global___OwnedVideoFrameBuffer = OwnedVideoFrameBuffer

@typing_extensions.final
class PlanarYuvBufferInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHROMA_WIDTH_FIELD_NUMBER: builtins.int
    CHROMA_HEIGHT_FIELD_NUMBER: builtins.int
    STRIDE_Y_FIELD_NUMBER: builtins.int
    STRIDE_U_FIELD_NUMBER: builtins.int
    STRIDE_V_FIELD_NUMBER: builtins.int
    STRIDE_A_FIELD_NUMBER: builtins.int
    DATA_Y_PTR_FIELD_NUMBER: builtins.int
    DATA_U_PTR_FIELD_NUMBER: builtins.int
    DATA_V_PTR_FIELD_NUMBER: builtins.int
    DATA_A_PTR_FIELD_NUMBER: builtins.int
    chroma_width: builtins.int
    chroma_height: builtins.int
    stride_y: builtins.int
    stride_u: builtins.int
    stride_v: builtins.int
    stride_a: builtins.int
    data_y_ptr: builtins.int
    """*const u8 or *const u16"""
    data_u_ptr: builtins.int
    data_v_ptr: builtins.int
    data_a_ptr: builtins.int
    """nullptr = no alpha"""
    def __init__(
        self,
        *,
        chroma_width: builtins.int = ...,
        chroma_height: builtins.int = ...,
        stride_y: builtins.int = ...,
        stride_u: builtins.int = ...,
        stride_v: builtins.int = ...,
        stride_a: builtins.int = ...,
        data_y_ptr: builtins.int = ...,
        data_u_ptr: builtins.int = ...,
        data_v_ptr: builtins.int = ...,
        data_a_ptr: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["chroma_height", b"chroma_height", "chroma_width", b"chroma_width", "data_a_ptr", b"data_a_ptr", "data_u_ptr", b"data_u_ptr", "data_v_ptr", b"data_v_ptr", "data_y_ptr", b"data_y_ptr", "stride_a", b"stride_a", "stride_u", b"stride_u", "stride_v", b"stride_v", "stride_y", b"stride_y"]) -> None: ...

global___PlanarYuvBufferInfo = PlanarYuvBufferInfo

@typing_extensions.final
class BiplanarYuvBufferInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHROMA_WIDTH_FIELD_NUMBER: builtins.int
    CHROMA_HEIGHT_FIELD_NUMBER: builtins.int
    STRIDE_Y_FIELD_NUMBER: builtins.int
    STRIDE_UV_FIELD_NUMBER: builtins.int
    DATA_Y_PTR_FIELD_NUMBER: builtins.int
    DATA_UV_PTR_FIELD_NUMBER: builtins.int
    chroma_width: builtins.int
    chroma_height: builtins.int
    stride_y: builtins.int
    stride_uv: builtins.int
    data_y_ptr: builtins.int
    data_uv_ptr: builtins.int
    def __init__(
        self,
        *,
        chroma_width: builtins.int = ...,
        chroma_height: builtins.int = ...,
        stride_y: builtins.int = ...,
        stride_uv: builtins.int = ...,
        data_y_ptr: builtins.int = ...,
        data_uv_ptr: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["chroma_height", b"chroma_height", "chroma_width", b"chroma_width", "data_uv_ptr", b"data_uv_ptr", "data_y_ptr", b"data_y_ptr", "stride_uv", b"stride_uv", "stride_y", b"stride_y"]) -> None: ...

global___BiplanarYuvBufferInfo = BiplanarYuvBufferInfo

@typing_extensions.final
class NativeBufferInfo(google.protobuf.message.Message):
    """TODO(theomonnom): Expose graphic context?"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___NativeBufferInfo = NativeBufferInfo

@typing_extensions.final
class VideoStreamInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    type: global___VideoStreamType.ValueType
    def __init__(
        self,
        *,
        type: global___VideoStreamType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["type", b"type"]) -> None: ...

global___VideoStreamInfo = VideoStreamInfo

@typing_extensions.final
class OwnedVideoStream(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HANDLE_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    @property
    def handle(self) -> handle_pb2.FfiOwnedHandle: ...
    @property
    def info(self) -> global___VideoStreamInfo: ...
    def __init__(
        self,
        *,
        handle: handle_pb2.FfiOwnedHandle | None = ...,
        info: global___VideoStreamInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["handle", b"handle", "info", b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["handle", b"handle", "info", b"info"]) -> None: ...

global___OwnedVideoStream = OwnedVideoStream

@typing_extensions.final
class VideoStreamEvent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STREAM_HANDLE_FIELD_NUMBER: builtins.int
    FRAME_RECEIVED_FIELD_NUMBER: builtins.int
    EOS_FIELD_NUMBER: builtins.int
    stream_handle: builtins.int
    @property
    def frame_received(self) -> global___VideoFrameReceived: ...
    @property
    def eos(self) -> global___VideoStreamEOS: ...
    def __init__(
        self,
        *,
        stream_handle: builtins.int = ...,
        frame_received: global___VideoFrameReceived | None = ...,
        eos: global___VideoStreamEOS | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["eos", b"eos", "frame_received", b"frame_received", "message", b"message"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["eos", b"eos", "frame_received", b"frame_received", "message", b"message", "stream_handle", b"stream_handle"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["message", b"message"]) -> typing_extensions.Literal["frame_received", "eos"] | None: ...

global___VideoStreamEvent = VideoStreamEvent

@typing_extensions.final
class VideoFrameReceived(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FRAME_FIELD_NUMBER: builtins.int
    BUFFER_FIELD_NUMBER: builtins.int
    @property
    def frame(self) -> global___VideoFrameInfo: ...
    @property
    def buffer(self) -> global___OwnedVideoFrameBuffer: ...
    def __init__(
        self,
        *,
        frame: global___VideoFrameInfo | None = ...,
        buffer: global___OwnedVideoFrameBuffer | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["buffer", b"buffer", "frame", b"frame"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["buffer", b"buffer", "frame", b"frame"]) -> None: ...

global___VideoFrameReceived = VideoFrameReceived

@typing_extensions.final
class VideoStreamEOS(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___VideoStreamEOS = VideoStreamEOS

@typing_extensions.final
class VideoSourceResolution(google.protobuf.message.Message):
    """
    VideoSource
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WIDTH_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    width: builtins.int
    height: builtins.int
    def __init__(
        self,
        *,
        width: builtins.int = ...,
        height: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["height", b"height", "width", b"width"]) -> None: ...

global___VideoSourceResolution = VideoSourceResolution

@typing_extensions.final
class VideoSourceInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    type: global___VideoSourceType.ValueType
    def __init__(
        self,
        *,
        type: global___VideoSourceType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["type", b"type"]) -> None: ...

global___VideoSourceInfo = VideoSourceInfo

@typing_extensions.final
class OwnedVideoSource(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HANDLE_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    @property
    def handle(self) -> handle_pb2.FfiOwnedHandle: ...
    @property
    def info(self) -> global___VideoSourceInfo: ...
    def __init__(
        self,
        *,
        handle: handle_pb2.FfiOwnedHandle | None = ...,
        info: global___VideoSourceInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["handle", b"handle", "info", b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["handle", b"handle", "info", b"info"]) -> None: ...

global___OwnedVideoSource = OwnedVideoSource
