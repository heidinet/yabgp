# Copyright 2015-2017 Cisco Systems, Inc.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import struct

from yabgp.message.attribute.linkstate.linkstate import LinkState
from yabgp.message import TLV


@LinkState.register(typecode=1089, typestr='maximum-link-bandwidth')
@LinkState.register(typecode=1090, typestr='maximum-reserved-link-bandwidth')
class LinkBandWidth(TLV):

    @classmethod
    def parse(cls, value):
        """
        """
        return cls(value=struct.unpack('!f', value)[0])