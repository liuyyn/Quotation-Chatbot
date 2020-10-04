import React, { Component } from "react";
import Bubble from "./Bubble";
import Text from "./Text";
import { Card, CardTitle } from "reactstrap";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getBotMessage } from "./redux/actions/messageActions";

class Chatbot extends Component {
  static propTypes = {
    messages: PropTypes.object.isRequired,
    getBotMessage: PropTypes.func.isRequired,
  };

  render() {
    return (
      <div>
        <Card>
          <CardTitle>Mr Health Quotation</CardTitle>
          {this.props.messages.messages.map((d) => (
            <Bubble key={d.message} message={d.message} person={d.person} />
          ))}
          <Text />
        </Card>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  messages: state.messages,
});

export default connect(mapStateToProps, { getBotMessage })(Chatbot);
