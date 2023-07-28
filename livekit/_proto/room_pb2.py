# Copyright 2023 LiveKit, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: room.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import handle_pb2 as handle__pb2
from . import participant_pb2 as participant__pb2
from . import track_pb2 as track__pb2
from . import video_frame_pb2 as video__frame__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nroom.proto\x12\rlivekit.proto\x1a\x0chandle.proto\x1a\x11participant.proto\x1a\x0btrack.proto\x1a\x11video_frame.proto\"Y\n\x0e\x43onnectRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\x12+\n\x07options\x18\x03 \x01(\x0b\x32\x1a.livekit.proto.RoomOptions\">\n\x0f\x43onnectResponse\x12+\n\x08\x61sync_id\x18\x01 \x01(\x0b\x32\x19.livekit.proto.FfiAsyncId\"\x83\x01\n\x0f\x43onnectCallback\x12+\n\x08\x61sync_id\x18\x01 \x01(\x0b\x32\x19.livekit.proto.FfiAsyncId\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x12%\n\x04room\x18\x03 \x01(\x0b\x32\x17.livekit.proto.RoomInfoB\x08\n\x06_error\"D\n\x11\x44isconnectRequest\x12/\n\x0broom_handle\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\"A\n\x12\x44isconnectResponse\x12+\n\x08\x61sync_id\x18\x01 \x01(\x0b\x32\x19.livekit.proto.FfiAsyncId\"A\n\x12\x44isconnectCallback\x12+\n\x08\x61sync_id\x18\x01 \x01(\x0b\x32\x19.livekit.proto.FfiAsyncId\"\xad\x01\n\x13PublishTrackRequest\x12/\n\x0broom_handle\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\x12\x30\n\x0ctrack_handle\x18\x02 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\x12\x33\n\x07options\x18\x03 \x01(\x0b\x32\".livekit.proto.TrackPublishOptions\"C\n\x14PublishTrackResponse\x12+\n\x08\x61sync_id\x18\x01 \x01(\x0b\x32\x19.livekit.proto.FfiAsyncId\"\x9b\x01\n\x14PublishTrackCallback\x12+\n\x08\x61sync_id\x18\x01 \x01(\x0b\x32\x19.livekit.proto.FfiAsyncId\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x38\n\x0bpublication\x18\x03 \x01(\x0b\x32#.livekit.proto.TrackPublicationInfoB\x08\n\x06_error\"v\n\x15UnpublishTrackRequest\x12/\n\x0broom_handle\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\x12\x19\n\x11stop_on_unpublish\x18\x03 \x01(\x08\"E\n\x16UnpublishTrackResponse\x12+\n\x08\x61sync_id\x18\x01 \x01(\x0b\x32\x19.livekit.proto.FfiAsyncId\"c\n\x16UnpublishTrackCallback\x12+\n\x08\x61sync_id\x18\x01 \x01(\x0b\x32\x19.livekit.proto.FfiAsyncId\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_error\"\xb1\x01\n\x12PublishDataRequest\x12/\n\x0broom_handle\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\x12\x10\n\x08\x64\x61ta_ptr\x18\x02 \x01(\x04\x12\x11\n\tdata_size\x18\x03 \x01(\x04\x12+\n\x04kind\x18\x04 \x01(\x0e\x32\x1d.livekit.proto.DataPacketKind\x12\x18\n\x10\x64\x65stination_sids\x18\x05 \x03(\t\"B\n\x13PublishDataResponse\x12+\n\x08\x61sync_id\x18\x01 \x01(\x0b\x32\x19.livekit.proto.FfiAsyncId\"`\n\x13PublishDataCallback\x12+\n\x08\x61sync_id\x18\x01 \x01(\x0b\x32\x19.livekit.proto.FfiAsyncId\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_error\"\x86\x01\n\x14SetSubscribedRequest\x12/\n\x0broom_handle\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\x12\x11\n\tsubscribe\x18\x02 \x01(\x08\x12\x17\n\x0fparticipant_sid\x18\x03 \x01(\t\x12\x11\n\ttrack_sid\x18\x04 \x01(\t\"\x17\n\x15SetSubscribedResponse\";\n\rVideoEncoding\x12\x13\n\x0bmax_bitrate\x18\x01 \x01(\x04\x12\x15\n\rmax_framerate\x18\x02 \x01(\x01\"$\n\rAudioEncoding\x12\x13\n\x0bmax_bitrate\x18\x01 \x01(\x04\"\x8a\x02\n\x13TrackPublishOptions\x12\x34\n\x0evideo_encoding\x18\x01 \x01(\x0b\x32\x1c.livekit.proto.VideoEncoding\x12\x34\n\x0e\x61udio_encoding\x18\x02 \x01(\x0b\x32\x1c.livekit.proto.AudioEncoding\x12.\n\x0bvideo_codec\x18\x03 \x01(\x0e\x32\x19.livekit.proto.VideoCodec\x12\x0b\n\x03\x64tx\x18\x04 \x01(\x08\x12\x0b\n\x03red\x18\x05 \x01(\x08\x12\x11\n\tsimulcast\x18\x06 \x01(\x08\x12*\n\x06source\x18\x07 \x01(\x0e\x32\x1a.livekit.proto.TrackSource\"P\n\x0bRoomOptions\x12\x16\n\x0e\x61uto_subscribe\x18\x01 \x01(\x08\x12\x17\n\x0f\x61\x64\x61ptive_stream\x18\x02 \x01(\x08\x12\x10\n\x08\x64ynacast\x18\x03 \x01(\x08\"\xf5\t\n\tRoomEvent\x12/\n\x0broom_handle\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\x12\x44\n\x15participant_connected\x18\x02 \x01(\x0b\x32#.livekit.proto.ParticipantConnectedH\x00\x12J\n\x18participant_disconnected\x18\x03 \x01(\x0b\x32&.livekit.proto.ParticipantDisconnectedH\x00\x12\x43\n\x15local_track_published\x18\x04 \x01(\x0b\x32\".livekit.proto.LocalTrackPublishedH\x00\x12G\n\x17local_track_unpublished\x18\x05 \x01(\x0b\x32$.livekit.proto.LocalTrackUnpublishedH\x00\x12\x38\n\x0ftrack_published\x18\x06 \x01(\x0b\x32\x1d.livekit.proto.TrackPublishedH\x00\x12<\n\x11track_unpublished\x18\x07 \x01(\x0b\x32\x1f.livekit.proto.TrackUnpublishedH\x00\x12:\n\x10track_subscribed\x18\x08 \x01(\x0b\x32\x1e.livekit.proto.TrackSubscribedH\x00\x12>\n\x12track_unsubscribed\x18\t \x01(\x0b\x32 .livekit.proto.TrackUnsubscribedH\x00\x12K\n\x19track_subscription_failed\x18\n \x01(\x0b\x32&.livekit.proto.TrackSubscriptionFailedH\x00\x12\x30\n\x0btrack_muted\x18\x0b \x01(\x0b\x32\x19.livekit.proto.TrackMutedH\x00\x12\x34\n\rtrack_unmuted\x18\x0c \x01(\x0b\x32\x1b.livekit.proto.TrackUnmutedH\x00\x12G\n\x17\x61\x63tive_speakers_changed\x18\r \x01(\x0b\x32$.livekit.proto.ActiveSpeakersChangedH\x00\x12M\n\x1a\x63onnection_quality_changed\x18\x0e \x01(\x0b\x32\'.livekit.proto.ConnectionQualityChangedH\x00\x12\x34\n\rdata_received\x18\x0f \x01(\x0b\x32\x1b.livekit.proto.DataReceivedH\x00\x12I\n\x18\x63onnection_state_changed\x18\x10 \x01(\x0b\x32%.livekit.proto.ConnectionStateChangedH\x00\x12-\n\tconnected\x18\x11 \x01(\x0b\x32\x18.livekit.proto.ConnectedH\x00\x12\x33\n\x0c\x64isconnected\x18\x12 \x01(\x0b\x32\x1b.livekit.proto.DisconnectedH\x00\x12\x33\n\x0creconnecting\x18\x13 \x01(\x0b\x32\x1b.livekit.proto.ReconnectingH\x00\x12\x31\n\x0breconnected\x18\x14 \x01(\x0b\x32\x1a.livekit.proto.ReconnectedH\x00\x42\t\n\x07message\"\xd4\x01\n\x08RoomInfo\x12*\n\x06handle\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\x12\x0b\n\x03sid\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08metadata\x18\x04 \x01(\t\x12\x39\n\x11local_participant\x18\x05 \x01(\x0b\x32\x1e.livekit.proto.ParticipantInfo\x12\x34\n\x0cparticipants\x18\x06 \x03(\x0b\x32\x1e.livekit.proto.ParticipantInfo\"D\n\x14ParticipantConnected\x12,\n\x04info\x18\x01 \x01(\x0b\x32\x1e.livekit.proto.ParticipantInfo\"G\n\x17ParticipantDisconnected\x12,\n\x04info\x18\x01 \x01(\x0b\x32\x1e.livekit.proto.ParticipantInfo\"x\n\x13LocalTrackPublished\x12\x38\n\x0bpublication\x18\x01 \x01(\x0b\x32#.livekit.proto.TrackPublicationInfo\x12\'\n\x05track\x18\x02 \x01(\x0b\x32\x18.livekit.proto.TrackInfo\"0\n\x15LocalTrackUnpublished\x12\x17\n\x0fpublication_sid\x18\x01 \x01(\t\"c\n\x0eTrackPublished\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x38\n\x0bpublication\x18\x02 \x01(\x0b\x32#.livekit.proto.TrackPublicationInfo\"D\n\x10TrackUnpublished\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x17\n\x0fpublication_sid\x18\x02 \x01(\t\"S\n\x0fTrackSubscribed\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\'\n\x05track\x18\x02 \x01(\x0b\x32\x18.livekit.proto.TrackInfo\"?\n\x11TrackUnsubscribed\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\"T\n\x17TrackSubscriptionFailed\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"8\n\nTrackMuted\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\":\n\x0cTrackUnmuted\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\"1\n\x15\x41\x63tiveSpeakersChanged\x12\x18\n\x10participant_sids\x18\x01 \x03(\t\"f\n\x18\x43onnectionQualityChanged\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x31\n\x07quality\x18\x02 \x01(\x0e\x32 .livekit.proto.ConnectionQuality\"\xbe\x01\n\x0c\x44\x61taReceived\x12*\n\x06handle\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\x12\x1c\n\x0fparticipant_sid\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x08\x64\x61ta_ptr\x18\x03 \x01(\x04\x12\x11\n\tdata_size\x18\x04 \x01(\x04\x12+\n\x04kind\x18\x05 \x01(\x0e\x32\x1d.livekit.proto.DataPacketKindB\x12\n\x10_participant_sid\"G\n\x16\x43onnectionStateChanged\x12-\n\x05state\x18\x01 \x01(\x0e\x32\x1e.livekit.proto.ConnectionState\"\x0b\n\tConnected\"\x0e\n\x0c\x44isconnected\"\x0e\n\x0cReconnecting\"\r\n\x0bReconnected*N\n\x11\x43onnectionQuality\x12\x10\n\x0cQUALITY_POOR\x10\x00\x12\x10\n\x0cQUALITY_GOOD\x10\x01\x12\x15\n\x11QUALITY_EXCELLENT\x10\x02*S\n\x0f\x43onnectionState\x12\x15\n\x11\x43ONN_DISCONNECTED\x10\x00\x12\x12\n\x0e\x43ONN_CONNECTED\x10\x01\x12\x15\n\x11\x43ONN_RECONNECTING\x10\x02*3\n\x0e\x44\x61taPacketKind\x12\x0e\n\nKIND_LOSSY\x10\x00\x12\x11\n\rKIND_RELIABLE\x10\x01\x42\x10\xaa\x02\rLiveKit.Protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'room_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\rLiveKit.Proto'
  _globals['_CONNECTIONQUALITY']._serialized_start=5048
  _globals['_CONNECTIONQUALITY']._serialized_end=5126
  _globals['_CONNECTIONSTATE']._serialized_start=5128
  _globals['_CONNECTIONSTATE']._serialized_end=5211
  _globals['_DATAPACKETKIND']._serialized_start=5213
  _globals['_DATAPACKETKIND']._serialized_end=5264
  _globals['_CONNECTREQUEST']._serialized_start=94
  _globals['_CONNECTREQUEST']._serialized_end=183
  _globals['_CONNECTRESPONSE']._serialized_start=185
  _globals['_CONNECTRESPONSE']._serialized_end=247
  _globals['_CONNECTCALLBACK']._serialized_start=250
  _globals['_CONNECTCALLBACK']._serialized_end=381
  _globals['_DISCONNECTREQUEST']._serialized_start=383
  _globals['_DISCONNECTREQUEST']._serialized_end=451
  _globals['_DISCONNECTRESPONSE']._serialized_start=453
  _globals['_DISCONNECTRESPONSE']._serialized_end=518
  _globals['_DISCONNECTCALLBACK']._serialized_start=520
  _globals['_DISCONNECTCALLBACK']._serialized_end=585
  _globals['_PUBLISHTRACKREQUEST']._serialized_start=588
  _globals['_PUBLISHTRACKREQUEST']._serialized_end=761
  _globals['_PUBLISHTRACKRESPONSE']._serialized_start=763
  _globals['_PUBLISHTRACKRESPONSE']._serialized_end=830
  _globals['_PUBLISHTRACKCALLBACK']._serialized_start=833
  _globals['_PUBLISHTRACKCALLBACK']._serialized_end=988
  _globals['_UNPUBLISHTRACKREQUEST']._serialized_start=990
  _globals['_UNPUBLISHTRACKREQUEST']._serialized_end=1108
  _globals['_UNPUBLISHTRACKRESPONSE']._serialized_start=1110
  _globals['_UNPUBLISHTRACKRESPONSE']._serialized_end=1179
  _globals['_UNPUBLISHTRACKCALLBACK']._serialized_start=1181
  _globals['_UNPUBLISHTRACKCALLBACK']._serialized_end=1280
  _globals['_PUBLISHDATAREQUEST']._serialized_start=1283
  _globals['_PUBLISHDATAREQUEST']._serialized_end=1460
  _globals['_PUBLISHDATARESPONSE']._serialized_start=1462
  _globals['_PUBLISHDATARESPONSE']._serialized_end=1528
  _globals['_PUBLISHDATACALLBACK']._serialized_start=1530
  _globals['_PUBLISHDATACALLBACK']._serialized_end=1626
  _globals['_SETSUBSCRIBEDREQUEST']._serialized_start=1629
  _globals['_SETSUBSCRIBEDREQUEST']._serialized_end=1763
  _globals['_SETSUBSCRIBEDRESPONSE']._serialized_start=1765
  _globals['_SETSUBSCRIBEDRESPONSE']._serialized_end=1788
  _globals['_VIDEOENCODING']._serialized_start=1790
  _globals['_VIDEOENCODING']._serialized_end=1849
  _globals['_AUDIOENCODING']._serialized_start=1851
  _globals['_AUDIOENCODING']._serialized_end=1887
  _globals['_TRACKPUBLISHOPTIONS']._serialized_start=1890
  _globals['_TRACKPUBLISHOPTIONS']._serialized_end=2156
  _globals['_ROOMOPTIONS']._serialized_start=2158
  _globals['_ROOMOPTIONS']._serialized_end=2238
  _globals['_ROOMEVENT']._serialized_start=2241
  _globals['_ROOMEVENT']._serialized_end=3510
  _globals['_ROOMINFO']._serialized_start=3513
  _globals['_ROOMINFO']._serialized_end=3725
  _globals['_PARTICIPANTCONNECTED']._serialized_start=3727
  _globals['_PARTICIPANTCONNECTED']._serialized_end=3795
  _globals['_PARTICIPANTDISCONNECTED']._serialized_start=3797
  _globals['_PARTICIPANTDISCONNECTED']._serialized_end=3868
  _globals['_LOCALTRACKPUBLISHED']._serialized_start=3870
  _globals['_LOCALTRACKPUBLISHED']._serialized_end=3990
  _globals['_LOCALTRACKUNPUBLISHED']._serialized_start=3992
  _globals['_LOCALTRACKUNPUBLISHED']._serialized_end=4040
  _globals['_TRACKPUBLISHED']._serialized_start=4042
  _globals['_TRACKPUBLISHED']._serialized_end=4141
  _globals['_TRACKUNPUBLISHED']._serialized_start=4143
  _globals['_TRACKUNPUBLISHED']._serialized_end=4211
  _globals['_TRACKSUBSCRIBED']._serialized_start=4213
  _globals['_TRACKSUBSCRIBED']._serialized_end=4296
  _globals['_TRACKUNSUBSCRIBED']._serialized_start=4298
  _globals['_TRACKUNSUBSCRIBED']._serialized_end=4361
  _globals['_TRACKSUBSCRIPTIONFAILED']._serialized_start=4363
  _globals['_TRACKSUBSCRIPTIONFAILED']._serialized_end=4447
  _globals['_TRACKMUTED']._serialized_start=4449
  _globals['_TRACKMUTED']._serialized_end=4505
  _globals['_TRACKUNMUTED']._serialized_start=4507
  _globals['_TRACKUNMUTED']._serialized_end=4565
  _globals['_ACTIVESPEAKERSCHANGED']._serialized_start=4567
  _globals['_ACTIVESPEAKERSCHANGED']._serialized_end=4616
  _globals['_CONNECTIONQUALITYCHANGED']._serialized_start=4618
  _globals['_CONNECTIONQUALITYCHANGED']._serialized_end=4720
  _globals['_DATARECEIVED']._serialized_start=4723
  _globals['_DATARECEIVED']._serialized_end=4913
  _globals['_CONNECTIONSTATECHANGED']._serialized_start=4915
  _globals['_CONNECTIONSTATECHANGED']._serialized_end=4986
  _globals['_CONNECTED']._serialized_start=4988
  _globals['_CONNECTED']._serialized_end=4999
  _globals['_DISCONNECTED']._serialized_start=5001
  _globals['_DISCONNECTED']._serialized_end=5015
  _globals['_RECONNECTING']._serialized_start=5017
  _globals['_RECONNECTING']._serialized_end=5031
  _globals['_RECONNECTED']._serialized_start=5033
  _globals['_RECONNECTED']._serialized_end=5046
# @@protoc_insertion_point(module_scope)
