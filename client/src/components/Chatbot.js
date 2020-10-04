import React from "react";
import Bubble from "./Bubble";
import Text from "./Text";
import { Card, CardTitle } from "reactstrap";

function Chatbot() {
  const state = {
    messages: ["Hello", "How are you?"],
  };

  return (
    <div>
      <Card>
        <CardTitle>Mr Health Quotation</CardTitle>
        {state.messages.map((m) => (
          <Bubble key={m} message={m} />
        ))}

        <Text />
      </Card>
    </div>
  );
}

export default Chatbot;
