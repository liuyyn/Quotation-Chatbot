import React, { Component } from "react";
import { Form, FormGroup, Input } from "reactstrap";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addUserMessage, getBotMessage } from "./redux/actions/messageActions";

class Text extends Component {
  state = {
    message: "",
  };

  static propTypes = {
    addUserMessage: PropTypes.func.isRequired,
    getBotMessage: PropTypes.func.isRequired,
  };

  onChange = (e) => {
    this.setState({
      message: e.target.value,
    });
  };

  onSubmit = (e) => {
    e.preventDefault();

    e.target.reset();

    this.props.addUserMessage({ person: "You", message: this.state.message });

    this.props.getBotMessage(this.state.message);
  };

  render() {
    return (
      <>
        <Form onSubmit={this.onSubmit}>
          {/* <Form> */}
          <FormGroup>
            <Input placeholder="Ask a question" onChange={this.onChange} />
            {/* <Button>Send</Button> */}
          </FormGroup>
        </Form>
      </>
    );
  }
}

const mapStateToProps = (state) => ({
  messages: state.messages,
});

export default connect(mapStateToProps, { addUserMessage, getBotMessage })(
  Text
);
