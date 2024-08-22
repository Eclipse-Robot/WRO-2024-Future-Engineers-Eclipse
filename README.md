<!-- Banner -->

<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Eclipse-Robot/WRO-2024-Future-Engineers-Eclipse/blob/main/other/img/Eclipse.png">
 <source media="(prefers-color-scheme: light)" srcset="https://github.com/Eclipse-Robot/WRO-2024-Future-Engineers-Eclipse/blob/main/other/img/Eclipse.png">
 <img alt="Eclipse's banner" src="https://github.com/Eclipse-Robot/WRO-2024-Future-Engineers-Eclipse/blob/main/other/img/Eclipse.png">
</picture>
<br>
<!-- Banner End -->

<!-- Progression -->

<details open>
<summary><big>Progression</big></summary>

<h2>How we discovered Future Engineers</h2>
<p>First, we heard about Future Engineer at the end of our 2024 RobotMission senior <abbr title="World Robot Olympiad">WRO</abbr> trial. After the medals were awarded, the head judge presented this competition. She mentioned that it was more challenging and complex than what we had previously experienced. On the way back home, we discussed it with our coach, who thought it was a great project for us and encouraged us to participate. He promised to provide us with as many resources as we needed, both human and material. We felt excited knowing that we had full access to all of the newest technology at the school (3D printers, laser cutter, etc.). So, here we were, one week after our previous competition, in the technology room, paper and pencil in hand, ready to create a masterpiece.</p>


</details>

<!-- Progression End-->

<!-- Mobility Managment -->
<details open> <summary><big>Mobility Managment</big></summary>
<h2>The motors</h2>
<p>
<br>First, the robot is moving with two motors, one for the speed and the other for the direction.
<ul>
<li>The first one is a DC motor that come from an arduino kit (Smart Robot Car Kit 3.0):<br>
<img alt="DC Motor" src="https://github.com/Eclipse-Robot/WRO-2024-Future-Engineers-Eclipse/blob/main/other/img/DC_Motor.png?raw=true"   width="200" height="200"> <br> We chose this one over others because we had plenty on hand and found them to be reliable for our needs (they are durable, can maintain precise speeds, and can reverse). It is constantly powered, so the vehicle is always in motion.</li><br><br>

<li>The other one is a micro servo motor SG90:<br>
<img alt="SG90 Motor" src="https://github.com/Eclipse-Robot/WRO-2024-Future-Engineers-Eclipse/blob/main/other/img/SG90.png?raw=true"  width="200" height="200"> <br> Its small and very precise gears made it the perfect candidate for our direction system, which sometimes needs to turn to a precise angle. This one is almost always powered because it constantly needs to make micro adjustments.</li>
</ul><br>

<h2>Chassis</h2>

For the vehicle chassis, we 3D printed an F1 car shape so the wheels could turn without contacting the structure. We made sure to leave enough space for the Raspberry Pi, Arduino, motor driver, and camera.<br>

The technical drawing of the chassis:<br>
<img alt="Chassis" src="https://github.com/Eclipse-Robot/WRO-2024-Future-Engineers-Eclipse/blob/main/other/img/Drawing/Drawing%20Base.png?raw=true"  width="300" height="200"><br>

Before we arrived at this final version, we had other designs. The most notable one is this, where we combined all the robot’s components into a single piece. It was too complex and took too long to print, so we abandoned the idea:<br>
<img alt="Chassis V1" src="https://github.com/Eclipse-Robot/WRO-2024-Future-Engineers-Eclipse/blob/main/other/img/Drawing/Drawing%20Base%20V1.png?raw=true"  width="300" height="200">

<br>

<h2>Direction system</h2>


</p>


</details>
<!-- Mobility Managment End-->



<!-- Power and Sense Managment -->
<details open>
<summary><big>Power and Sense Managment</big></summary>
<h2>Battery</h2>
<p>
The vehicle is powered by two distinct power sources:
<ul>
<li>
PiSugar 3 Plus Battery: This battery is dedicated to powering the Raspberry Pi 4B, ensuring a stable and reliable energy supply for processing tasks, camera operation, and fans.</li><br><br>

<li>External Battery: The motor driver (L298N) and the motor draw power from an external battery, whose voltage must be carefully chosen to meet the requirements of the motor driver and motors. This battery powers the high-energy consuming components, ensuring that the motors receive sufficient power for movement.</li><br><br>
</ul>
The vehicle also uses a Camera Module 3 Wide to capture visual information, enabling it to navigate and detect obstacles. This camera is connected directly to the Raspberry Pi, which processes the image data and makes decisions based on the visual input.<br><br>
Each component's power consumption is carefully managed to optimize the vehicle's efficiency. The Raspberry Pi's power needs are met by the PiSugar 3 Plus battery, while the more power-intensive motors are powered by the external battery. Balancing these power demands ensures that the vehicle operates effectively without overloading any single power source.<br><br>


</p>

</details>
<!-- Power and Sense Managment End-->



<!-- Obstacle Managment -->
<details open>
<summary><big>Obstacle Managment</big></summary>
<h2>Camera</h2>

<p>
Fot the camera we made yet another 3D model


</p>

</details>
<!-- Obstacle Managment End-->



<!-- Pictures – Team and vehicle -->
<details open>
<summary><big>Pictures – Team and vehicle</big></summary>


</details>
<!-- Pictures – Team and vehicle End-->



<!-- Performance Video -->
<details open>
<summary><big>Performance Video</big></summary>


</details>
<!-- Performance Video End-->



<!-- Engineering Factor -->
<details open>
<summary><big>Engineering Factor</big></summary>

<h2>Materials:</h2>

<ul>
  <li>
  <a href="https://www.pishop.ca/product/raspberry-pi-4-model-b-8gb/">Raspberry Pi 4 Model B/8GB, </a>
  </li>

  <li>
  <a href="https://www.pishop.ca/product/raspberry-pi-camera-module-3-wide/">Raspberry Pi Camera Module 3 Wide</a>
  </li>

  <li>
  <a href="https://www.tindie.com/products/pisugar/pisugar-3-plus-battery-for-raspberry-pi-3b3b4b/">Pisugar 3 Plus: Battery for Raspberry Pi 3B/3B+/4B</a>
  </li>

  <li>
  <a href="https://www.pishop.ca/product/diy-jumper-wires-for-raspberry-pi-30cm//">Male to Female Jumper Cable x 40 (20cm)</a>
  </li>

  <li>
  <a href="https://www.pishop.ca/product/dual-fan-for-raspberry-pi/">Dual Fan for Raspberry Pi</a>
  </li>

  <li>
  <a href="https://www.pishop.ca/product/raspberry-pi-15w-power-supply-us-black/">Raspberry Pi 15W USB-C Power Supply, US, Black</a>
  </li>

  <li>
  <a href="https://www.pishop.ca/product/microhdmi-hdmi-cable-6ft/">Micro-HDMI to HDMI cable for Pi 4, 6ft, Black</a>
  </li>

  <li>
  <a href="https://www.elegoo.com/en-ca/products/elegoo-smart-robot-car-kit-v-3-0-plus/">Smart Robot Car Kit V3.0 Plus</a>
  </li>

 <li>
  <a href="https://store-usa.arduino.cc/products/arduino-starter-kit-multi-language?selectedStore=us">Arduino Starter Kit Multi-language (Arduino Uno R3 included)</a>
  </li>

  <li>
  <a href="https://www.pishop.ca/product/microsd-card-64-gb-class-10-blank/">MicroSD Card - 64 GB - Class 10 - BLANK</a>
  </li>

</ul>


</details>
<!-- Engineering Factor End-->


<details open>
<summary><big>Random information</big></summary>

<h2>Weight<h2>

<p>- Raspberry Pi, Camera, Pisugar and DualFan = 170.42 g <br> 
- Arduino = 22.69g <br>
- 4x wheels = 138.74g <br>
- Battery for engines = 125.95g
</p>

</details>

