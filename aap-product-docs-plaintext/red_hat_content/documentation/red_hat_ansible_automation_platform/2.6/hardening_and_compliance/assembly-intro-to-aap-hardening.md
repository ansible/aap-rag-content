# Chapter 1. Introduction to hardening Ansible Automation Platform




This document provides guidance for improving the security posture (referred to as “hardening” throughout this guide) of your Red Hat Ansible Automation Platform deployment on Red Hat Enterprise Linux.

The following are not currently within the scope of this guide:

- Other deployment targets for Ansible Automation Platform, such as OpenShift.
- Ansible Automation Platform managed services available through cloud service provider marketplaces.


Note
Hardening and compliance for Ansible Automation Platform 2.4 includes additional considerations with regards to the specific _Defense Security Information Agency_ (DISA) _Security Technical Implementation Guides_ (STIGs) for automation controller, but this guidance does not apply to Ansible Automation Platform 2.6.



This guide takes a practical approach to hardening the Ansible Automation Platform security posture, starting with the planning and architecture phase of deployment and then covering specific guidance for installation, initial configuration, and day 2 operations. As this guide specifically covers Ansible Automation Platform running on Red Hat Enterprise Linux, hardening guidance for Red Hat Enterprise Linux will be covered where it affects the automation platform components. Additional considerations with regards to the DISA STIGs for Red Hat Enterprise Linux are provided for those organizations that integrate the DISA STIGs as a part of their overall security strategy.

Note
These recommendations do not guarantee security or compliance of your deployment of Ansible Automation Platform. You must assess security from the unique requirements of your organization to address specific threats and risks and balance these against implementation factors.



