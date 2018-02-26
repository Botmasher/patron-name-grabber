import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import url from 'url';
// patreon
import patreonAPI, { oauth as patreonOAuth } from 'patreon';

const CLIENT_ID = 'nsiLILh-CHqeNKLuQn5hkJ6CwniKzaa4fqj9tXFL2onvoLqbQjui1Oqe8BIoy2zl';
const CLIENT_SECRET = 'rQBnNdjz0VDdkZXaQQc36RglMumfzk2PHa-6TXgU8vPkvuzDIgPQrho6jTiJNoBm';
const patreonOAuthClient = patreonOAuth(CLIENT_ID, CLIENT_SECRET);

const redirectURL = 'http://www.nativlang.com/';

function handleOAuthRedirectRequest(requestUrl, response) {
  const oauthGrantCode = url.parse(requestUrl, true).query.code;
  patreonOAuthClient
    .getTokens(oauthGrantCode, redirectURL)
      .then(tokensResponse => {
        const patreonAPIClient = patreonAPI(tokensResponse.access_token)
        return patreonAPIClient('/current_user')
      })
      .then(({ store }) => {
        // store is a [JsonApiDataStore](https://github.com/beauby/jsonapi-datastore)
        // You can also ask for result.rawJson if you'd like to work with unparsed data
        response.end(store.findAll('user').map(user => user.serialize()))
      })
      .catch(err => {
        console.error('error!', err)
        response.end(err)
      });
}

const api_address='https://www.patreon.com/api/oauth2/api/current_user';

const headers={
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer gemtsIcSAiiolo0zcswFPrzXLFXhS6tycOaQOM6QHjc',
  'Access-Control-Allow-Origin': "http://localhost:3000"
};

const get = (endpoint="", method='GET', body=null) => {
  const attributes = body !== null ? {headers, method, body: JSON.stringify(body)} : {headers, method};
  return fetch(`${api_address}/${endpoint}`, attributes)
    .then(response => {
      return response.json();
    });
};

//export const getPatronInfo = patronId => get(`${endpoints.posts}/${patronId}`);

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      patronData: {}
    };
  }

  componentDidMount() {
    //get().then(data => this.setState({patronData: data}));
    handleOAuthRedirectRequest(api_address);
  }

  render() {
    console.log(this.state.patronData);
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Patron Name Grabber</h1>
        </header>
        <p className="App-intro">
          Test page for patron name grabber interface.
        </p>
      </div>
    );
  }
}

export default App;
