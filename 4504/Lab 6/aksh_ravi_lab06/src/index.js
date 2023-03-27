import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const Lab06App = function (props) {
  return (
    <main>
      <Title title="Lab06 - React Application" />
      <Catalog />
    </main>
  );
}

const root = ReactDOM.createRoot(document.getElementById("react-lab"));
root.render(<Lab06App />)

const Title = function (props) {
  return <h1>{props.title}</h1>;
}

class Catalog extends React.Component {
  constructor(props) {
    super(props);
    this.state = {editing: false, filename: "images/img1.jpg", alt: "Image 1: Raptor" };
    this.handleNameChange = this.handleNameChange.bind(this);
    this.handleAltChange = this.handleAltChange.bind(this);
  }

  editClick = () => {
    this.setState({editing: true});
  }

  saveClick = () => {
    this.setState({editing: false});
  }

  handleNameChange(event) {
    const image = event.target.value;
    this.setState({filename: image});
  }

  handleAltChange(event) {
    const altText = event.target.value;
    this.setState({alt: altText});
  }

  renderNormal() {
    return (
      <div>
        <h2>{this.state.alt}</h2>
        <img src={this.state.filename} alt={this.state.alt} onClick={this.editClick} />
      </div>
    );
  }

  renderEdit() {
    return (
      <div>
        <p>
          <select onChange={this.handleNameChange}>
            <option value="images/img1.jpg">Image 1</option>
            <option value="images/img2.jpg">Image 2</option>
            <option value="images/img3.jpg">Image 3</option>
            <option value="images/img4.jpg">Image 4</option>
          </select>
        </p>
        <p>
          <label for="altText">ALT Text for selected image: </label>
          <input name="altText" onChange={this.handleAltChange}/>
        </p>
        <button type="submit" onClick={this.saveClick}>Save</button>
      </div>
    );
  }

  render() {
    if (this.state.editing) {
      return(this.renderEdit());
    }
    else{
      return(this.renderNormal());
    }
  }
}

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
