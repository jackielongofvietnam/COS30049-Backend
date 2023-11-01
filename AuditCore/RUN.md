# Documentation on how to run locally

## 1. Activate the environment
`cd AuditCore`

`. ./SlitherEnv/bin/activate`

## 2. Setup 


`cd slither`
`python3 setup.py install`

## 3. Install a solc compiler

`pip install solc-select`
`solc-select install 0.8.13`
`solc-select install 0.5.0`

## 4. Select a solidity compiler

Depending on the compiler version of your desired solidity file, use the compiler that matches the one in `.sol` file. For example, if my `.sol` file looks like this:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;


```

It means that you should use the version of `0.5.0`. Below is how you can switch to a version `0.5.0`:

`solc-select use 0.5.0`

## Detect vulnerabilities

**Remember:** The `.sol` file must be inside the `slither` folder. Also, you should go back to AuditCore folder.

Then you execute the command:

`python Execute.py`

then, you need to enter the filename with extension `.sol`

The expected output looks like this:

```shell
(Slither) (base) tamvo@Tams-MacBook-Air Audit % python Execute.py
Enter filename: killbilly.sol
{'Issue': 'KillBilly.commencekilling() (killbilly.sol#21-24) allows anyone to destruct the contract\n', 'Suggestion': 'Protect access to all sensitive functions.\n\n\n\n'}

{'Issue': 'KillBilly.activatekillability() (killbilly.sol#16-19) compares to a boolean constant:\n\t-require(bool)(approved_killers[msg.sender] == true) (killbilly.sol#17)\n', 'Suggestion': 'Remove the equality to the boolean constant.\n\n\n\n'}

{'Issue': 'Pragma version^0.5.0 (killbilly.sol#2) allows old versions\nsolc-0.5.0 is not recommended for deployment\n', 'Suggestion': '\n\nDeploy with any of the following Solidity versions:\n\n- 0.8.18\n\n\n\nThe recommendations take into account:\n\n- Risks related to recent releases\n\n- Risks of complex code generation changes\n\n- Risks of new language features\n\n- Risks of known bugs\n\n\n\nUse a simple pragma version that allows any of these versions.\n\nConsider using the latest version of Solidity for testing.\n\n\n\n'}

{'Issue': 'Variable KillBilly.is_killable (killbilly.sol#5) is not in mixedCase\nVariable KillBilly.approved_killers (killbilly.sol#6) is not in mixedCase\n', 'Suggestion': 'Follow the Solidity [naming convention](https://solidity.readthedocs.io/en/v0.4.25/style-guide.html#naming-conventions).\n\n\n\n'}


```

