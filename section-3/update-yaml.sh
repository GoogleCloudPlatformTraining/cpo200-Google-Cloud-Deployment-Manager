#! /bin/bash
# Copyright 2016 Google Inc.
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

source ~/cpo200/config

sed -i \
-e s/'<your-default-region>'/$CPO200_REGION/ \
-e s/'<your-default-zone>'/$CPO200_ZONE/ \
-e s/'<your-sql-region>'/$CPO200_SQL_REGION/ \
-e s/'<guestbook-sql-password>'/$CPO200_SQL_PW/ \
-e s/'<startup-scripts-bucket>'/$CPO200_SCRIPTS_BUCKET/ \
guestbook.yaml