import React, { Component } from "react";
import { Button, Form, FormGroup, Input } from "reactstrap";

class Text extends Component {
  state = {
    message: "",
  };

  onChange = (e) => {
    this.setState({
      message: e.target.value,
    });
  };

  //   onSubmit = (e) => {
  //     e.preventDefault();

  //     // this.props.addMessage()
  //   };

  render() {
    return (
      <>
        {/* <Form onSubmit={this.onSubmit()}> */}
        <Form>
          <FormGroup>
            <Input placeholder="Ask a question" onChange={this.onChange} />
            <Button>Send</Button>
          </FormGroup>
        </Form>
      </>
    );
  }
}

export default Text;
