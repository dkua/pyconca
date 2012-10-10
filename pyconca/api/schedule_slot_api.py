from pyconca.api.base_api import BaseApi
from pyconca.dao.schedule_slot_dao import ScheduleSlotDao


class ScheduleSlotApi(BaseApi):

    def _configure(self):
        self.name = 'schedule_slot'
        self.dao = ScheduleSlotDao(self.request.user)
        self.schema = None

    def _post_process_for_output(self, model, output):
        new_output = output.copy()
        if model.talk:
            new_output['talk_id'] = model.talk.id
        else:
            new_output['talk_id'] = None
        return new_output
