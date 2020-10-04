import React, { Component } from "react";
import Bubble from "./Bubble";
import Text from "./Text";
import { Card, CardTitle } from "reactstrap";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getBotMessage } from "./redux/actions/messageActions";
import { v4 as uuid } from "uuid";

class Chatbot extends Component {
  static propTypes = {
    messages: PropTypes.object.isRequired,
    getBotMessage: PropTypes.func.isRequired,
  };

  render() {
    return (
      <div className="scroll">
        <Card>
          <CardTitle>Mr Health Quotation</CardTitle>
          <div className="bubbles">
            {this.props.messages.messages.map((d) => (
              <Bubble key={uuid()} message={d.message} person={d.person} />
            ))}
          </div>

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
