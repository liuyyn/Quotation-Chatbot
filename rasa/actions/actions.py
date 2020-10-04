# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Text, List, Dict, Any

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.interfaces import Action

from typing import Dict, Text, List, Any


from typing import Dict, Text, List


class AskForAgeAction(Action):
    def name(self) -> Text:
        return "action_ask_age"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="How old are you?")
        return []

class AskForSexAction(Action):
    def name(self) -> Text:
        return "action_ask_sex"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="What is your gender?")
        return []

class AskForBmiAction(Action):
    def name(self) -> Text:
        return "action_ask_bmi"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="What is your body mass index?")
        return []

class AskForChildrenAction(Action):
    def name(self) -> Text:
        return "action_ask_children"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="How many children do you have? You should enter 0 if you don't have any.")
        return []

class AskForSmokerAction(Action):
    def name(self) -> Text:
        return "action_ask_smoker"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="Have you smoked at least once in the past year?")
        return []


class ActionGreet(Action):
    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_greet")
        return []


class ProfileForm(Action):
    def name(self) -> Text:
        return "profile_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        extracted_slots: Dict[Text, Any] = tracker.form_slots_to_validate()

        filled_characteristics = []

        for slot_name, slot_value in extracted_slots:
            # Check if slot is filled.
            if is_filled(slot_value):
                filled_characteristics.append(SlotSet(slot_name, slot_value))
            # else:
                # Return a `SlotSet` event with value `None` to indicate that this
                # slot still needs to be filled.
                # validation_events.append(SlotSet(slot_name, None))

        return validation_events

    def is_filled(slot_value: Any) -> bool:
        if slot_value == None:
            return False
        else:
            return True
        # Implementation of the is_filled function.





class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    @staticmethod
    def fetch_slots(tracker: Tracker) -> List[EventType]:
        """Collect slots that contain the user's name and phone number."""

        slots = []

        for key in ("name", "phone_number"):
            value = tracker.get_slot(key)
            if value is not None:
                slots.append(SlotSet(key=key, value=value))

        return slots

    async def run(
        self,
        output_channel: "OutputChannel",
        nlg: "NaturalLanguageGenerator",
        tracker: "DialogueStateTracker",
        domain: "Domain",
    ) -> List[Event]:

        # the session should begin with a `session_started` event
        events = [SessionStarted(metadata=self.metadata)]

        # any slots that should be carried over should come after the
        # `session_started` event
        events.extend(self.fetch_slots(tracker))

        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))

        return events
