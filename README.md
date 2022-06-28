# StrangerOnMyPC
Protect your personal computer against unauthorized access from strangers using this utility

## But, what does it actually do?
Well it creates some sort of isolated user profile on your Windows PC and restricts almost all of it's privileges, such as accessing network drives attached to This PC, and modifying or installing new software, accessing other people's profiles, modifying PC settings, even accessing local disk drives can be restricted using this tool.

## Is it available for commerical use?
Yes, This program is completely free and open-source, which means that you don't have to buy any sort of special licenses to use it in your organization.

## Limitations:
Every piece of software have their limitations, well, since this one counts also as a piece of software, it also has limitations, and they are:
* You need to set a password for your Administrator account(profile) (basically the profile you are executing this program from) to protect your PC against unauthorized administrative actions.
* This program might not function properly on Windows versions older than Windows 7 (SP1) (x64) Due to the limitations of the operating system itself and the way this program is designed to work.
* This program ***WILL NOT protect your computer*** if the profile you are running it is not an **Administrator account**.

## That seems interesting, Can I use it now?
**No, You can't**

Because it is still in the `beta testing` phase, which means that most of it's features aren't complete and might not function as intended.

## What features does it offer right now?
It is still in the `beta testing` phase, which means that most of it's features aren't complete yet and might not function as intended, but here is a list of all features right there.
* It is still a **Python 3.x.x** script file (Meaning it is still in it's `alpha` or `Dev` stages yet and can't be used by **Non-Python programmers**)

However despite that, the program still works like a charm, with the following list of all features available:
* It can create an isolated user profile.
* That profile can't set a password for themselves.
* That profile will have a name of "**Guest on This PC**"
* You can rename that account later after you create it **(of course using the call of an appropriate Python 3.x.x function for that purpose)**.
* It has a splash screen that shows upon the login of the **Guest** account that tells them they are running on a restricted user profile (Might not function as intended as this feature is not complete yet)

## Disclaimer
**Despite being functional and useful on my personal PC, I can't guarantee that it will even start on your PC (of course due to differences in CPU architectures and OS base), but however the chances are higher than expected that it will work for you (if you have your PC properly configured)**
