---
layout: default
title: FAQ
nav_order: 2
has_children: false
---

# Frequently asked questions
{: .mb-5}

<details markdown="block">
  <summary class="fs-5 mb-3">
    How many players can OWS support?
  </summary>

With OWS 2 our goal is to support 100,000 concurrent players or more. This will be heavily dependent on your game and server hardware.
</details>

<details markdown="block">
  <summary class="fs-5 mb-3">
    Are transitions between Zone Server Instances seamless?
  </summary>

Seamless transitions are not currently supported in OWS 2. While seamless transitions are achievable, by default Unreal Engine does not support it. OWS uses Unreal Engine's client travel system which by default unloads the current map before loading the new one.
</details>

<details markdown="block">
  <summary class="fs-5 mb-3">
    Can players on one Zone Server Instance see players on another Zone Server Instance?
  </summary>

This is not supported by default, but there is nothing stopping you from sending data between the Zone Server Instances to achieve this.  This may be something OWS 2 addresses in the future.
</details>

<details markdown="block">
  <summary class="fs-5 mb-3">
    How many players can each Zone Server Instance support?
  </summary>

As OWS 2 is using Unreal Engine's instance server, you are limited by whatever limitations Unreal Engine's server instances have.  OWS 2 does nothing to change this as OWS 2 is not a Game server.  Epic released a [video](https://www.youtube.com/watch?v=CDnNAAzgltw) about optimizing the Data which gets send from and to the server using a custom Replication Graph. Fortnite, for example, supports up to 100 players per Zone Instance.
</details>
