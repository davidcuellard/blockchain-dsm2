import React, { useEffect, useState } from "react";
import Web3 from "web3";
import contractAbi from "../config/contractABI.json"; // Replace with your contract's ABI
import "./SmartContract.css";

const ethers = require("ethers");

function SmartContract() {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);
  const [contract, setContract] = useState(null);
  const [msgCat, setMsgCat] = useState("");
  const [authorizedListers, setAuthorizedListers] = useState([]);
  const [authorizedPurchasers, setAuthorizedPurchasers] = useState([]);
  const [newAuthorizedAddress, setNewAuthorizedAddress] = useState("");
  const [connected, setConnected] = useState(false);
  const [bandId, setBandId] = useState("");
  const [state, setState] = useState("");

  async function initializeWeb3() {
    if (window.ethereum) {
      try {
        const web3Instance = new Web3(window.ethereum);
        const accounts = await web3Instance.eth.getAccounts();
        setWeb3(web3Instance);
        setAccount(accounts[0]);
        setConnected(true);
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        const contractInstance = new ethers.Contract(
          "0x902261248155B62a06395479ecB0807768e458db", // Replace with your contract's address
          contractAbi,
          signer
        );
        setContract(contractInstance);
      } catch (error) {
        console.error("Error connecting to MetaMask:", error);
      }
    } else {
      console.error("MetaMask not detected.");
    }
  }

  useEffect(() => {
    initializeWeb3();
  }, []);

  async function connectWallet() {
    await initializeWeb3();
  }

  function disconnectWallet() {
    setWeb3(null);
    setAccount(null);
    setContract(null);
    setConnected(false);
  }

  async function removeAuthorized() {
    if (contract && newAuthorizedAddress) {
      try {
        await contract.removeAuthorized([newAuthorizedAddress]);
        console.log("Authorized address removed successfully!");
        setNewAuthorizedAddress("");
        await getAuthorizedUsers();
      } catch (error) {
        console.error("Error removing authorized address:", error);
      }
    }
  }

  async function setAuthorized() {
    if (contract && newAuthorizedAddress) {
      try {
        await contract.setAuthorized([newAuthorizedAddress]);
        console.log("Authorized address set successfully!");
        setNewAuthorizedAddress("");
        await getAuthorizedUsers();
      } catch (error) {
        console.error("Error setting authorized address:", error);
      }
    }
  }

  async function getMessages() {
    if (contract) {
      try {
        const messageCat = await contract.message();
        setMsgCat(messageCat);
      } catch (error) {
        console.error("Error getting messages:", error);
      }
    }
  }

  async function getAuthorizedUsers() {
    if (contract) {
      try {
        const listerCount = await contract.authorizedListersCount();
        const purchaserCount = await contract.authorizedPurchasersCount();
        const listers = [];
        const purchasers = [];

        for (let i = 0; i < listerCount; i++) {
          const address = await contract.authorizedListers(i);
          listers.push(address);
        }

        for (let i = 0; i < purchaserCount; i++) {
          const address = await contract.authorizedPurchasers(i);
          purchasers.push(address);
        }

        setAuthorizedListers(listers);
        setAuthorizedPurchasers(purchasers);
      } catch (error) {
        console.error("Error getting authorized users:", error);
      }
    }
  }

  async function requestCat() {
    if (contract && bandId !== "") {
      try {
        const tx = await contract.requestCat(Number(bandId));
        await tx.wait();
        console.log("Cat request successful!");
      } catch (error) {
        console.error("Error sending cat request:", error);
      }
    }
  }

  async function requestListing() {
    if (contract && bandId !== "" && state !== "") {
      try {
        const tx = await contract.requestListing(Number(bandId), Number(state));
        await tx.wait();
        console.log("Listing request successful!");
      } catch (error) {
        console.error("Error sending listing request:", error);
      }
    }
  }

  return (
    <div className="container">
      <div>User Account: {account}</div>
      {connected ? (
        <div>
          <button className="disconnect-btn" onClick={disconnectWallet}>
            Disconnect Wallet
          </button>
          <div className="button-group">
            <input
              type="text"
              placeholder="Band ID"
              value={bandId}
              onChange={(e) => setBandId(e.target.value)}
            />
            <input
              type="text"
              placeholder="State"
              value={state}
              onChange={(e) => setState(e.target.value)}
            />
            <button className="action-btn" onClick={requestCat}>
              Request Cat
            </button>
          </div>
          <div className="message-cat">
            <button className="action-btn" onClick={getMessages}>
              Get Messages
            </button>
            <div>Message Cat: {msgCat}</div>
          </div>

          {/* <div className="authorized-users">
            <strong>Authorized Users:</strong>
            <div>
              {authorizedListers.map((address, index) => (
                <div key={index}>
                  Authorized Lister {index + 1}: {address}
                </div>
              ))}
            </div>
            <div>
              {authorizedPurchasers.map((address, index) => (
                <div key={index}>
                  Authorized Purchaser {index + 1}: {address}
                </div>
              ))}
            </div>
          </div>

          <div className="action-group">
            <input
              type="text"
              placeholder="Enter address"
              value={newAuthorizedAddress}
              onChange={(e) => setNewAuthorizedAddress(e.target.value)}
            />
            <button className="action-btn" onClick={removeAuthorized}>
              Remove Authorized
            </button>
            <button className="action-btn" onClick={setAuthorized}>
              Set Authorized
            </button>
          </div> */}
        </div>
      ) : (
        <button className="connect-wallet-btn" onClick={connectWallet}>
          Connect Wallet
        </button>
      )}
    </div>
  );
}

export default SmartContract;
