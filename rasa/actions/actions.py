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




from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.interfaces import Action

from rasa_sdk.forms import FormAction

from typing import Any, Text, Dict, List, Union



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


class ProfileForm(FormAction):

    def name(self):
        return "profile_form"

    @staticmethod
    def required_slots(tracker):
        return ["age", "sex", "bmi", "children", "smoker"]

    """def run(
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

        return filled_characteristics

    def is_filled(slot_value: Any) -> bool:
        if slot_value == None:
            return False
        else:
            return True
        # Implementation of the is_filled function."""


    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"age": self.from_entity(entity="age",
                                            intent="inform"),
                "sex": self.from_entity(entity="sex",
                                            intent="inform"),
                "bmi": self.from_entity(entity="bmi",
                                            intent="inform"),
                "children": self.from_entity(entity="children",
                                            intent="inform"),
                "smoker": self.from_entity(entity="smoker",
                                            intent="inform")
                }
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message("Thanks, great job!")
        return []


