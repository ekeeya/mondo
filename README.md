<div id="top"></div>

<!--[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="kintu/static/landing/assets/img/favicon/favicon.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Easy USSD with intuitive flows</h3>

  <p align="center">
    An awesome way to manage your USSD menus!
    <br>
    What if you don't need a technical person to change your USSD menus?
    <br />
    <a href="https://mondo.oddjobs/docs"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://mondo.oddjobs/demo">View Demo</a>
    ·
    <a href="https://github.com/ekeeya/mondo">Report Bug</a>
    ·
    <a href="https://github.com/ekeeya/mondo/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<!--<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>-->



<!-- ABOUT THE PROJECT -->
## About The Project

[![Easy USSD][product-screenshot]](https://mondo.oddjobs.tech)

We have carefully looked around the web for this kind of solution but to our surprise, there isn't any (or at least not
open source). 
For most of the years we have spent building USSD applications, we have noticed that our clients rely on us to make 
changes to USSD menus whenever need arises. Normally, we achieve this by jumping into code or the database or some 
kind of menu generating engine to make the necessary amendments. 
With help from amazing graphic flows, <!--[Nyaruka Flow Editor](https://github.com/nyaruka/floweditor)-->, we have put 
up a 
solution 
to allow none-technical personnel have the power to create, update, delete Items from a USSD menu as well as linking 
making Items on the menu do other things in the background, for example link to an external API, send mails, save 
data to a database,send sms, you name it.

Do not get us wrong, we have seen some attempts to solve this issue but most of the solutions still help experienced 
developers some use [yaml](https://yaml.org/) files, (yeah, I bet you know what yaml is,.. if you do, congs! ). 
Basically, our solution will eliminate a developer completely when it comes to menus.
Let us know if you have seen any similar solutions, so we do not waste time re-inventing the wheel.

#### What is USSD?
The [wikipedia](https://en.wikipedia.org/wiki/Unstructured_Supplementary_Service_Data) definition of USSD is; 

Unstructured Supplementary Service Data (USSD), sometimes referred to as "quick codes" or "feature codes", is a communications protocol used by GSM cellular telephones to communicate with the mobile network operator's computers. USSD can be used for WAP browsing, prepaid callback service, mobile-money services, location-based content services, menu-based information services, and as part of configuring the phone on the network.
#### Which USSD Menu are we talking about?

Let's jog your memory a little, have you ever been in a situation where your Mobile 
Network Operator (MNO) e.g MTN, AT&T etc instructs you to dial a shortcode (*211#) in order for you to subscribe to a 
hot 
promotion deal or access a give new (always eye-catching) service?

Once you dial this shortcode (*211#), you will be presented with a menu of possible selections for example;
```angular2html
Welcome to ABC Bank services
1. Login
2. Register
3. Quit
```
Normally, what happens is, this request is pushed to your MNO who later forwards  it to an aggregator (USSD gateway),
in 
some 
cases the MNO it's self does the aggregation, the aggregator then routes this request via HTTP to a server 
application that processes the request basing on the parameters therein and also processes the next menu, the response 
follows the same reverse route back to the end User (Mobile phone).

#### Where does this solution enter the equation?
This solution is focusing all its energy on menu generation using intuitive graphic flows that anyone can play about 
with. We intend to develop this solution so that a 6-year-old can use it.

On top of that, we also allow users do other actions midway a USSD flow, e.g if a user responds with option 1, the 
application should send an SMS, an email, or call an external entity with the user's parameters for whatever reasons.

We also know that multiple aggregators expect different parameters let alone their nomenclature in a request. So 
have developed this solution to allow users easily setup different handlers for different aggregators (USSD gateways).
For example [Africas talking](https://africastalking.com/ussd) 
```js
sessionId
serviceCode
phoneNumber
text
```
And [DMARK](https://dmarkmobile.com/) expects;
```js
session_id
timestamp
ussd_code
body
```
Clearly we have a problem here but the application allows you to configure multiple USSD gateways and assign them 
handlers so that we do not have a problem with parameter nomenclature or miss-out any mandatory params for a given 
gateway.

I know this sounds technical but think of it as a deployment step that is obviously done by a technical person. The 
only catch is, after all this, you will have the means to alter your USSD flows as you like even if you are not that
technical.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

This solution is developed using the following technologies;

* [Vue.js](https://vuejs.org/) for the user interface.
* [Spring boot](https://spring.io/projects/spring-boot)
* [Postgresql ](https://www.postgresql.org/)
* [Nyaruka Flow editor](https://www.npmjs.com/package/@nyaruka/flow-editor)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

coming soon 

### Prerequisites

coming soon

### Installation

<!--_Below is an example of how you can instruct your audience on installing and setting up your app. This template 
doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
-->
coming soon....
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

coming soon...
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] USSD Menu Management
    - [ ] UI flow editor <br>
      Cloning and customizing @nyaruka/flow editor<br>
        - [ ] Change wording on canvas before any nodes are created to <br> 
        - [ ] Modifying styling such that the width of the inner div inside a node is set to ```auto```.
        - [ ] Fix node character count to 160-182 (USSD standard)
        - [ ] Remove all that we do not need
    - [ ] Flow execution engine<br>
      Since the UI flow translates into JSON, we need an engine that traverses the nodes <br>
        - [ ] Traverse and execute Send USSD Message node
        - [ ] Traverse and execute Wait for response node"
        - [ ] Traverse and execute Send SMS node
        - [ ] Traverse and execute Send mail node
        - [ ] Traverse and execute Call webhook node
        - [ ] Traverse and execute Enter another flow node
        - [ ] Implement response Validators
    - [ ] USSD Flow APIs
       - [ ] Create, update, delete a flow
       - [ ] Export and import a flow in JSON format
    - [ ] USSD Gateway(Aggregators) 
       - [ ] Register, update, delete Aggregator
       - [ ] Configure Handlers
    - [ ] SMS Gateways
       - [ ] In-app kannel config and control
    - [ ] User Interface
       - [ ] Use Vue to connect to the API end points
    - [ ] Database
- [ ] Testing

See the [open issues](https://github.com/ekeeya/mondo/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Keeya Emmanuel Lubowa - [@keldoticom](https://twitter.com/keldoticom) - ekeeya@oddjobs.tech

Project Website: [Here](https://mondo.oddjobs.tech)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

coming soon

<p align="right">(<a href="#top">back to top</a>)</p>


[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/ekeeya/mondo//graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/ekeeya/mondo//network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/ekeeya/mondo//stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/ekeeya/mondo/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: kintu/static/landing/assets/img/easy-ussd.png