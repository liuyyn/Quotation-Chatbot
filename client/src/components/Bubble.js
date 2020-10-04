import React from "react";
import { Toast, ToastBody, ToastHeader } from "reactstrap";

function Bubble(props) {
  //   const state = {
  //     message: "Hello",
  //   };

  return (
    <div>
      <div className="p-3 my-2 rounded">
        <Toast>
          <ToastHeader>You</ToastHeader>
          <ToastBody className="user">{props.message}</ToastBody>
        </Toast>
      </div>
    </div>
  );
}

export default Bubble;
