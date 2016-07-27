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

from orchestra.tests.unit import base


class CyclicWorkflowConductorTest(base.WorkflowConductorTest):

    @classmethod
    def setUpClass(cls):
        cls.composer_name = 'reverse'
        super(CyclicWorkflowConductorTest, cls).setUpClass()

    def test_cycle(self):
        wf_name = 'cycle'

        wf_spec = self.wf_spec_cls(self._get_wf_def(wf_name))

        with self.assertRaises(Exception) as cm:
            self.composer._compose_wf_graph(wf_spec)

            self.assertEqual(
                'Cycle detected in reverse workflow.',
                str(cm.exception)
            )
