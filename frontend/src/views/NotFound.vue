
<template>
    <div>
      <div class=" d-flex flex-column align-items-center">
            <br/>
            <div class="d-flex mb-12">
                <b><i>Oops we couldn't find that page.</i></b>
            </div>
      </div>
      <div class="dinosaur">
        <div class="t-rex"></div>
        <div class="eye"></div>
        <div class="horizont"></div>
        <div class="mountain"></div>
        <div class="mountainSec"></div>
        <div class="mountainThrd"></div>
        <div class="cloud"></div>
        <div class="cloudSec"></div>
        <div class="cloudThrd"></div>
        <div class="pteroBox">
          <div class="ptero"></div>
        </div>
      </div>
    </div>
</template>
  
<script>
export default {
name: 'NotFound',
};
</script>
  
<style scoped>
@-webkit-keyframes move {
99.999% {
    left: -110%;
}
0%,
100% {
    left: 110%;
}
}
@-moz-keyframes move {
99.999% {
    left: -110%;
}
0%,
100% {
    left: 110%;
}
}
@-o-keyframes move {
99.999% {
    left: -110%;
}
0%,
100% {
    left: 110%;
}
}
@keyframes move {
99.999% {
    left: -110%;
}
0%,
100% {
    left: 110%;
}
}
@-webkit-keyframes blinking {
0%,
89.999%,
95.001%,
100% {
    box-shadow: 5px 10px 0 3px #eee;
}
90%,
95% {
    box-shadow: 5px 10px 0 3px #535353;
}
}
@-moz-keyframes blinking {
0%,
89.999%,
95.001%,
100% {
    box-shadow: 5px 10px 0 3px #eee;
}
90%,
95% {
    box-shadow: 5px 10px 0 3px #535353;
}
}
@-o-keyframes blinking {
0%,
89.999%,
95.001%,
100% {
    box-shadow: 5px 10px 0 3px #eee;
}
90%,
95% {
    box-shadow: 5px 10px 0 3px #535353;
}
}
@keyframes blinking {
0%,
89.999%,
95.001%,
100% {
    box-shadow: 5px 10px 0 3px #eee;
}
90%,
95% {
    box-shadow: 5px 10px 0 3px #535353;
}
}
@-webkit-keyframes run {
0%,
49.999%,
100% {
    box-shadow: 0px 0 0 3px #535353, 5px 0 0 3px #535353, 10px 0 0 3px #535353, 15px 0 0 3px #535353,
    20px 0 0 3px #535353, 25px 0 0 3px #535353, 30px 0 0 3px #535353, 35px 0 0 3px #535353,
    -5px 5px 0 3px #535353, 0px 5px 0 3px #535353, 5px 5px 0 3px #535353, 10px 5px 0 3px #535353,
    15px 5px 0 3px #535353, 20px 5px 0 3px #535353, 25px 5px 0 3px #535353, 30px 5px 0 3px #535353,
    35px 5px 0 3px #535353, 40px 5px 0 3px #535353, -5px 10px 0 3px #535353,
    0px 10px 0 3px #535353, 10px 10px 0 3px #535353, 15px 10px 0 3px #535353,
    20px 10px 0 3px #535353, 25px 10px 0 3px #535353, 30px 10px 0 3px #535353,
    35px 10px 0 3px #535353, 40px 10px 0 3px #535353, -5px 15px 0 3px #535353,
    0px 15px 0 3px #535353, 5px 15px 0 3px #535353, 10px 15px 0 3px #535353,
    15px 15px 0 3px #535353, 20px 15px 0 3px #535353, 25px 15px 0 3px #535353,
    30px 15px 0 3px #535353, 35px 15px 0 3px #535353, 40px 15px 0 3px #535353,
    -5px 20px 0 3px #535353, 0px 20px 0 3px #535353, 5px 20px 0 3px #535353,
    10px 20px 0 3px #535353, 15px 20px 0 3px #535353, 20px 20px 0 3px #535353,
    25px 20px 0 3px #535353, 30px 20px 0 3px #535353, 35px 20px 0 3px #535353,
    40px 20px 0 3px #535353, -5px 25px 0 3px #535353, 0px 25px 0 3px #535353,
    5px 25px 0 3px #535353, 10px 25px 0 3px #535353, 15px 25px 0 3px #535353,
    -5px 30px 0 3px #535353, 0px 30px 0 3px #535353, 5px 30px 0 3px #535353,
    10px 30px 0 3px #535353, 15px 30px 0 3px #535353, 20px 30px 0 3px #535353,
    25px 30px 0 3px #535353, 30px 30px 0 3px #535353, -65px 35px 0 3px #535353,
    -10px 35px 0 3px #535353, -5px 35px 0 3px #535353, 0px 35px 0 3px #535353,
    5px 35px 0 3px #535353, 10px 35px 0 3px #535353, -65px 40px 0 3px #535353,
    -20px 40px 0 3px #535353, -15px 40px 0 3px #535353, -10px 40px 0 3px #535353,
    -5px 40px 0 3px #535353, 0px 40px 0 3px #535353, 5px 40px 0 3px #535353,
    10px 40px 0 3px #535353, -65px 45px 0 3px #535353, -60px 45px 0 3px #535353,
    -30px 45px 0 3px #535353, -25px 45px 0 3px #535353, -20px 45px 0 3px #535353,
    -15px 45px 0 3px #535353, -10px 45px 0 3px #535353, -5px 45px 0 3px #535353,
    0px 45px 0 3px #535353, 5px 45px 0 3px #535353, 10px 45px 0 3px #535353,
    15px 45px 0 3px #535353, 20px 45px 0 3px #535353, -65px 50px 0 3px #535353,
    -60px 50px 0 3px #535353, -55px 50px 0 3px #535353, -35px 50px 0 3px #535353,
    -30px 50px 0 3px #535353, -25px 50px 0 3px #535353, -20px 50px 0 3px #535353,
    -15px 50px 0 3px #535353, -10px 50px 0 3px #535353, -5px 50px 0 3px #535353,
    0px 50px 0 3px #535353, 5px 50px 0 3px #535353, 10px 50px 0 3px #535353,
    20px 50px 0 3px #535353, -65px 55px 0 3px #535353, -60px 55px 0 3px #535353,
    -55px 55px 0 3px #535353, -50px 55px 0 3px #535353, -45px 55px 0 3px #535353,
    -40px 55px 0 3px #535353, -35px 55px 0 3px #535353, -30px 55px 0 3px #535353,
    -25px 55px 0 3px #535353, -20px 55px 0 3px #535353, -15px 55px 0 3px #535353,
    -10px 55px 0 3px #535353, -5px 55px 0 3px #535353, 0px 55px 0 3px #535353,
    5px 55px 0 3px #535353, 10px 55px 0 3px #535353, -65px 60px 0 3px #535353,
    -60px 60px 0 3px #535353, -55px 60px 0 3px #535353, -50px 60px 0 3px #535353,
    -45px 60px 0 3px #535353, -40px 60px 0 3px #535353, -35px 60px 0 3px #535353,
    -30px 60px 0 3px #535353, -25px 60px 0 3px #535353, -20px 60px 0 3px #535353,
    -15px 60px 0 3px #535353, -10px 60px 0 3px #535353, -5px 60px 0 3px #535353,
    0px 60px 0 3px #535353, 5px 60px 0 3px #535353, 10px 60px 0 3px #535353,
    -60px 65px 0 3px #535353, -55px 65px 0 3px #535353, -50px 65px 0 3px #535353,
    -45px 65px 0 3px #535353, -40px 65px 0 3px #535353, -35px 65px 0 3px #535353,
    -30px 65px 0 3px #535353, -25px 65px 0 3px #535353, -20px 65px 0 3px #535353,
    -15px 65px 0 3px #535353, -10px 65px 0 3px #535353, -5px 65px 0 3px #535353,
    0px 65px 0 3px #535353, 5px 65px 0 3px #535353, -55px 70px 0 3px #535353,
    -50px 70px 0 3px #535353, -45px 70px 0 3px #535353, -40px 70px 0 3px #535353,
    -35px 70px 0 3px #535353, -30px 70px 0 3px #535353, -25px 70px 0 3px #535353,
    -20px 70px 0 3px #535353, -15px 70px 0 3px #535353, -10px 70px 0 3px #535353,
    -5px 70px 0 3px #535353, 0px 70px 0 3px #535353, 5px 70px 0 3px #535353,
    -50px 75px 0 3px #535353, -45px 75px 0 3px #535353, -40px 75px 0 3px #535353,
    -35px 75px 0 3px #535353, -30px 75px 0 3px #535353, -25px 75px 0 3px #535353,
    -20px 75px 0 3px #535353, -15px 75px 0 3px #535353, -10px 75px 0 3px #535353,
    -5px 75px 0 3px #535353, 0px 75px 0 3px #535353, -45px 80px 0 3px #535353,
    -40px 80px 0 3px #535353, -35px 80px 0 3px #535353, -30px 80px 0 3px #535353,
    -25px 80px 0 3px #535353, -20px 80px 0 3px #535353, -15px 80px 0 3px #535353,
    -10px 80px 0 3px #535353, -5px 80px 0 3px #535353, -40px 85px 0 3px #535353,
    -35px 85px 0 3px #535353, -30px 85px 0 3px #535353, -20px 85px 0 3px #535353,
    -15px 85px 0 3px #535353, -40px 90px 0 3px #535353, -35px 90px 0 3px #535353,
    -15px 90px 0 3px #535353, -10px 90px 0 3px #535353, -40px 95px 0 3px #535353,
    -40px 100px 0 3px #535353, -35px 100px 0 3px #535353;
}
50%,
99.999% {
    box-shadow: 0px 0 0 3px #535353, 5px 0 0 3px #535353, 10px 0 0 3px #535353, 15px 0 0 3px #535353,
    20px 0 0 3px #535353, 25px 0 0 3px #535353, 30px 0 0 3px #535353, 35px 0 0 3px #535353,
    -5px 5px 0 3px #535353, 0px 5px 0 3px #535353, 5px 5px 0 3px #535353, 10px 5px 0 3px #535353,
    15px 5px 0 3px #535353, 20px 5px 0 3px #535353, 25px 5px 0 3px #535353, 30px 5px 0 3px #535353,
    35px 5px 0 3px #535353, 40px 5px 0 3px #535353, -5px 10px 0 3px #535353,
    0px 10px 0 3px #535353, 10px 10px 0 3px #535353, 15px 10px 0 3px #535353,
    20px 10px 0 3px #535353, 25px 10px 0 3px #535353, 30px 10px 0 3px #535353,
    35px 10px 0 3px #535353, 40px 10px 0 3px #535353, -5px 15px 0 3px #535353,
    0px 15px 0 3px #535353, 5px 15px 0 3px #535353, 10px 15px 0 3px #535353,
    15px 15px 0 3px #535353, 20px 15px 0 3px #535353, 25px 15px 0 3px #535353,
    30px 15px 0 3px #535353, 35px 15px 0 3px #535353, 40px 15px 0 3px #535353,
    -5px 20px 0 3px #535353, 0px 20px 0 3px #535353, 5px 20px 0 3px #535353,
    10px 20px 0 3px #535353, 15px 20px 0 3px #535353, 20px 20px 0 3px #535353,
    25px 20px 0 3px #535353, 30px 20px 0 3px #535353, 35px 20px 0 3px #535353,
    40px 20px 0 3px #535353, -5px 25px 0 3px #535353, 0px 25px 0 3px #535353,
    5px 25px 0 3px #535353, 10px 25px 0 3px #535353, 15px 25px 0 3px #535353,
    -5px 30px 0 3px #535353, 0px 30px 0 3px #535353, 5px 30px 0 3px #535353,
    10px 30px 0 3px #535353, 15px 30px 0 3px #535353, 20px 30px 0 3px #535353,
    25px 30px 0 3px #535353, 30px 30px 0 3px #535353, -65px 35px 0 3px #535353,
    -10px 35px 0 3px #535353, -5px 35px 0 3px #535353, 0px 35px 0 3px #535353,
    5px 35px 0 3px #535353, 10px 35px 0 3px #535353, -65px 40px 0 3px #535353,
    -20px 40px 0 3px #535353, -15px 40px 0 3px #535353, -10px 40px 0 3px #535353,
    -5px 40px 0 3px #535353, 0px 40px 0 3px #535353, 5px 40px 0 3px #535353,
    10px 40px 0 3px #535353, -65px 45px 0 3px #535353, -60px 45px 0 3px #535353,
    -30px 45px 0 3px #535353, -25px 45px 0 3px #535353, -20px 45px 0 3px #535353,
    -15px 45px 0 3px #535353, -10px 45px 0 3px #535353, -5px 45px 0 3px #535353,
    0px 45px 0 3px #535353, 5px 45px 0 3px #535353, 10px 45px 0 3px #535353,
    15px 45px 0 3px #535353, 20px 45px 0 3px #535353, -65px 50px 0 3px #535353,
    -60px 50px 0 3px #535353, -55px 50px 0 3px #535353, -35px 50px 0 3px #535353,
    -30px 50px 0 3px #535353, -25px 50px 0 3px #535353, -20px 50px 0 3px #535353,
    -15px 50px 0 3px #535353, -10px 50px 0 3px #535353, -5px 50px 0 3px #535353,
    0px 50px 0 3px #535353, 5px 50px 0 3px #535353, 10px 50px 0 3px #535353,
    20px 50px 0 3px #535353, -65px 55px 0 3px #535353, -60px 55px 0 3px #535353,
    -55px 55px 0 3px #535353, -50px 55px 0 3px #535353, -45px 55px 0 3px #535353,
    -40px 55px 0 3px #535353, -35px 55px 0 3px #535353, -30px 55px 0 3px #535353,
    -25px 55px 0 3px #535353, -20px 55px 0 3px #535353, -15px 55px 0 3px #535353,
    -10px 55px 0 3px #535353, -5px 55px 0 3px #535353, 0px 55px 0 3px #535353,
    5px 55px 0 3px #535353, 10px 55px 0 3px #535353, -65px 60px 0 3px #535353,
    -60px 60px 0 3px #535353, -55px 60px 0 3px #535353, -50px 60px 0 3px #535353,
    -45px 60px 0 3px #535353, -40px 60px 0 3px #535353, -35px 60px 0 3px #535353,
    -30px 60px 0 3px #535353, -25px 60px 0 3px #535353, -20px 60px 0 3px #535353,
    -15px 60px 0 3px #535353, -10px 60px 0 3px #535353, -5px 60px 0 3px #535353,
    0px 60px 0 3px #535353, 5px 60px 0 3px #535353, 10px 60px 0 3px #535353,
    -60px 65px 0 3px #535353, -55px 65px 0 3px #535353, -50px 65px 0 3px #535353,
    -45px 65px 0 3px #535353, -40px 65px 0 3px #535353, -35px 65px 0 3px #535353,
    -30px 65px 0 3px #535353, -25px 65px 0 3px #535353, -20px 65px 0 3px #535353,
    -15px 65px 0 3px #535353, -10px 65px 0 3px #535353, -5px 65px 0 3px #535353,
    0px 65px 0 3px #535353, 5px 65px 0 3px #535353, -55px 70px 0 3px #535353,
    -50px 70px 0 3px #535353, -45px 70px 0 3px #535353, -40px 70px 0 3px #535353,
    -35px 70px 0 3px #535353, -30px 70px 0 3px #535353, -25px 70px 0 3px #535353,
    -20px 70px 0 3px #535353, -15px 70px 0 3px #535353, -10px 70px 0 3px #535353,
    -5px 70px 0 3px #535353, 0px 70px 0 3px #535353, 5px 70px 0 3px #535353,
    -50px 75px 0 3px #535353, -45px 75px 0 3px #535353, -40px 75px 0 3px #535353,
    -35px 75px 0 3px #535353, -30px 75px 0 3px #535353, -25px 75px 0 3px #535353,
    -20px 75px 0 3px #535353, -15px 75px 0 3px #535353, -10px 75px 0 3px #535353,
    -5px 75px 0 3px #535353, 0px 75px 0 3px #535353, -45px 80px 0 3px #535353,
    -40px 80px 0 3px #535353, -35px 80px 0 3px #535353, -30px 80px 0 3px #535353,
    -25px 80px 0 3px #535353, -20px 80px 0 3px #535353, -15px 80px 0 3px #535353,
    -10px 80px 0 3px #535353, -5px 80px 0 3px #535353, -40px 85px 0 3px #535353,
    -35px 85px 0 3px #535353, -20px 85px 0 3px #535353, -15px 85px 0 3px #535353,
    -35px 90px 0 3px #535353, -30px 90px 0 3px #535353, -15px 90px 0 3px #535353,
    -15px 95px 0 3px #535353, -15px 100px 0 3px #535353, -10px 100px 0 3px #535353;
}
}
@-moz-keyframes run {
0%,
49.999%,
100% {
    box-shadow: 0px 0 0 3px #535353, 5px 0 0 3px #535353, 10px 0 0 3px #535353, 15px 0 0 3px #535353,
    20px 0 0 3px #535353, 25px 0 0 3px #535353, 30px 0 0 3px #535353, 35px 0 0 3px #535353,
    -5px 5px 0 3px #535353, 0px 5px 0 3px #535353, 5px 5px 0 3px #535353, 10px 5px 0 3px #535353,
    15px 5px 0 3px #535353, 20px 5px 0 3px #535353, 25px 5px 0 3px #535353, 30px 5px 0 3px #535353,
    35px 5px 0 3px #535353, 40px 5px 0 3px #535353, -5px 10px 0 3px #535353,
    0px 10px 0 3px #535353, 10px 10px 0 3px #535353, 15px 10px 0 3px #535353,
    20px 10px 0 3px #535353, 25px 10px 0 3px #535353, 30px 10px 0 3px #535353,
    35px 10px 0 3px #535353, 40px 10px 0 3px #535353, -5px 15px 0 3px #535353,
    0px 15px 0 3px #535353, 5px 15px 0 3px #535353, 10px 15px 0 3px #535353,
    15px 15px 0 3px #535353, 20px 15px 0 3px #535353, 25px 15px 0 3px #535353,
    30px 15px 0 3px #535353, 35px 15px 0 3px #535353, 40px 15px 0 3px #535353,
    -5px 20px 0 3px #535353, 0px 20px 0 3px #535353, 5px 20px 0 3px #535353,
    10px 20px 0 3px #535353, 15px 20px 0 3px #535353, 20px 20px 0 3px #535353,
    25px 20px 0 3px #535353, 30px 20px 0 3px #535353, 35px 20px 0 3px #535353,
    40px 20px 0 3px #535353, -5px 25px 0 3px #535353, 0px 25px 0 3px #535353,
    5px 25px 0 3px #535353, 10px 25px 0 3px #535353, 15px 25px 0 3px #535353,
    -5px 30px 0 3px #535353, 0px 30px 0 3px #535353, 5px 30px 0 3px #535353,
    10px 30px 0 3px #535353, 15px 30px 0 3px #535353, 20px 30px 0 3px #535353,
    25px 30px 0 3px #535353, 30px 30px 0 3px #535353, -65px 35px 0 3px #535353,
    -10px 35px 0 3px #535353, -5px 35px 0 3px #535353, 0px 35px 0 3px #535353,
    5px 35px 0 3px #535353, 10px 35px 0 3px #535353, -65px 40px 0 3px #535353,
    -20px 40px 0 3px #535353, -15px 40px 0 3px #535353, -10px 40px 0 3px #535353,
    -5px 40px 0 3px #535353, 0px 40px 0 3px #535353, 5px 40px 0 3px #535353,
    10px 40px 0 3px #535353, -65px 45px 0 3px #535353, -60px 45px 0 3px #535353,
    -30px 45px 0 3px #535353, -25px 45px 0 3px #535353, -20px 45px 0 3px #535353,
    -15px 45px 0 3px #535353, -10px 45px 0 3px #535353, -5px 45px 0 3px #535353,
    0px 45px 0 3px #535353, 5px 45px 0 3px #535353, 10px 45px 0 3px #535353,
    15px 45px 0 3px #535353, 20px 45px 0 3px #535353, -65px 50px 0 3px #535353,
    -60px 50px 0 3px #535353, -55px 50px 0 3px #535353, -35px 50px 0 3px #535353,
    -30px 50px 0 3px #535353, -25px 50px 0 3px #535353, -20px 50px 0 3px #535353,
    -15px 50px 0 3px #535353, -10px 50px 0 3px #535353, -5px 50px 0 3px #535353,
    0px 50px 0 3px #535353, 5px 50px 0 3px #535353, 10px 50px 0 3px #535353,
    20px 50px 0 3px #535353, -65px 55px 0 3px #535353, -60px 55px 0 3px #535353,
    -55px 55px 0 3px #535353, -50px 55px 0 3px #535353, -45px 55px 0 3px #535353,
    -40px 55px 0 3px #535353, -35px 55px 0 3px #535353, -30px 55px 0 3px #535353,
    -25px 55px 0 3px #535353, -20px 55px 0 3px #535353, -15px 55px 0 3px #535353,
    -10px 55px 0 3px #535353, -5px 55px 0 3px #535353, 0px 55px 0 3px #535353,
    5px 55px 0 3px #535353, 10px 55px 0 3px #535353, -65px 60px 0 3px #535353,
    -60px 60px 0 3px #535353, -55px 60px 0 3px #535353, -50px 60px 0 3px #535353,
    -45px 60px 0 3px #535353, -40px 60px 0 3px #535353, -35px 60px 0 3px #535353,
    -30px 60px 0 3px #535353, -25px 60px 0 3px #535353, -20px 60px 0 3px #535353,
    -15px 60px 0 3px #535353, -10px 60px 0 3px #535353, -5px 60px 0 3px #535353,
    0px 60px 0 3px #535353, 5px 60px 0 3px #535353, 10px 60px 0 3px #535353,
    -60px 65px 0 3px #535353, -55px 65px 0 3px #535353, -50px 65px 0 3px #535353,
    -45px 65px 0 3px #535353, -40px 65px 0 3px #535353, -35px 65px 0 3px #535353,
    -30px 65px 0 3px #535353, -25px 65px 0 3px #535353, -20px 65px 0 3px #535353,
    -15px 65px 0 3px #535353, -10px 65px 0 3px #535353, -5px 65px 0 3px #535353,
    0px 65px 0 3px #535353, 5px 65px 0 3px #535353, -55px 70px 0 3px #535353,
    -50px 70px 0 3px #535353, -45px 70px 0 3px #535353, -40px 70px 0 3px #535353,
    -35px 70px 0 3px #535353, -30px 70px 0 3px #535353, -25px 70px 0 3px #535353,
    -20px 70px 0 3px #535353, -15px 70px 0 3px #535353, -10px 70px 0 3px #535353,
    -5px 70px 0 3px #535353, 0px 70px 0 3px #535353, 5px 70px 0 3px #535353,
    -50px 75px 0 3px #535353, -45px 75px 0 3px #535353, -40px 75px 0 3px #535353,
    -35px 75px 0 3px #535353, -30px 75px 0 3px #535353, -25px 75px 0 3px #535353,
    -20px 75px 0 3px #535353, -15px 75px 0 3px #535353, -10px 75px 0 3px #535353,
    -5px 75px 0 3px #535353, 0px 75px 0 3px #535353, -45px 80px 0 3px #535353,
    -40px 80px 0 3px #535353, -35px 80px 0 3px #535353, -30px 80px 0 3px #535353,
    -25px 80px 0 3px #535353, -20px 80px 0 3px #535353, -15px 80px 0 3px #535353,
    -10px 80px 0 3px #535353, -5px 80px 0 3px #535353, -40px 85px 0 3px #535353,
    -35px 85px 0 3px #535353, -30px 85px 0 3px #535353, -20px 85px 0 3px #535353,
    -15px 85px 0 3px #535353, -40px 90px 0 3px #535353, -35px 90px 0 3px #535353,
    -15px 90px 0 3px #535353, -10px 90px 0 3px #535353, -40px 95px 0 3px #535353,
    -40px 100px 0 3px #535353, -35px 100px 0 3px #535353;
}
50%,
99.999% {
    box-shadow: 0px 0 0 3px #535353, 5px 0 0 3px #535353, 10px 0 0 3px #535353, 15px 0 0 3px #535353,
    20px 0 0 3px #535353, 25px 0 0 3px #535353, 30px 0 0 3px #535353, 35px 0 0 3px #535353,
    -5px 5px 0 3px #535353, 0px 5px 0 3px #535353, 5px 5px 0 3px #535353, 10px 5px 0 3px #535353,
    15px 5px 0 3px #535353, 20px 5px 0 3px #535353, 25px 5px 0 3px #535353, 30px 5px 0 3px #535353,
    35px 5px 0 3px #535353, 40px 5px 0 3px #535353, -5px 10px 0 3px #535353,
    0px 10px 0 3px #535353, 10px 10px 0 3px #535353, 15px 10px 0 3px #535353,
    20px 10px 0 3px #535353, 25px 10px 0 3px #535353, 30px 10px 0 3px #535353,
    35px 10px 0 3px #535353, 40px 10px 0 3px #535353, -5px 15px 0 3px #535353,
    0px 15px 0 3px #535353, 5px 15px 0 3px #535353, 10px 15px 0 3px #535353,
    15px 15px 0 3px #535353, 20px 15px 0 3px #535353, 25px 15px 0 3px #535353,
    30px 15px 0 3px #535353, 35px 15px 0 3px #535353, 40px 15px 0 3px #535353,
    -5px 20px 0 3px #535353, 0px 20px 0 3px #535353, 5px 20px 0 3px #535353,
    10px 20px 0 3px #535353, 15px 20px 0 3px #535353, 20px 20px 0 3px #535353,
    25px 20px 0 3px #535353, 30px 20px 0 3px #535353, 35px 20px 0 3px #535353,
    40px 20px 0 3px #535353, -5px 25px 0 3px #535353, 0px 25px 0 3px #535353,
    5px 25px 0 3px #535353, 10px 25px 0 3px #535353, 15px 25px 0 3px #535353,
    -5px 30px 0 3px #535353, 0px 30px 0 3px #535353, 5px 30px 0 3px #535353,
    10px 30px 0 3px #535353, 15px 30px 0 3px #535353, 20px 30px 0 3px #535353,
    25px 30px 0 3px #535353, 30px 30px 0 3px #535353, -65px 35px 0 3px #535353,
    -10px 35px 0 3px #535353, -5px 35px 0 3px #535353, 0px 35px 0 3px #535353,
    5px 35px 0 3px #535353, 10px 35px 0 3px #535353, -65px 40px 0 3px #535353,
    -20px 40px 0 3px #535353, -15px 40px 0 3px #535353, -10px 40px 0 3px #535353,
    -5px 40px 0 3px #535353, 0px 40px 0 3px #535353, 5px 40px 0 3px #535353,
    10px 40px 0 3px #535353, -65px 45px 0 3px #535353, -60px 45px 0 3px #535353,
    -30px 45px 0 3px #535353, -25px 45px 0 3px #535353, -20px 45px 0 3px #535353,
    -15px 45px 0 3px #535353, -10px 45px 0 3px #535353, -5px 45px 0 3px #535353,
    0px 45px 0 3px #535353, 5px 45px 0 3px #535353, 10px 45px 0 3px #535353,
    15px 45px 0 3px #535353, 20px 45px 0 3px #535353, -65px 50px 0 3px #535353,
    -60px 50px 0 3px #535353, -55px 50px 0 3px #535353, -35px 50px 0 3px #535353,
    -30px 50px 0 3px #535353, -25px 50px 0 3px #535353, -20px 50px 0 3px #535353,
    -15px 50px 0 3px #535353, -10px 50px 0 3px #535353, -5px 50px 0 3px #535353,
    0px 50px 0 3px #535353, 5px 50px 0 3px #535353, 10px 50px 0 3px #535353,
    20px 50px 0 3px #535353, -65px 55px 0 3px #535353, -60px 55px 0 3px #535353,
    -55px 55px 0 3px #535353, -50px 55px 0 3px #535353, -45px 55px 0 3px #535353,
    -40px 55px 0 3px #535353, -35px 55px 0 3px #535353, -30px 55px 0 3px #535353,
    -25px 55px 0 3px #535353, -20px 55px 0 3px #535353, -15px 55px 0 3px #535353,
    -10px 55px 0 3px #535353, -5px 55px 0 3px #535353, 0px 55px 0 3px #535353,
    5px 55px 0 3px #535353, 10px 55px 0 3px #535353, -65px 60px 0 3px #535353,
    -60px 60px 0 3px #535353, -55px 60px 0 3px #535353, -50px 60px 0 3px #535353,
    -45px 60px 0 3px #535353, -40px 60px 0 3px #535353, -35px 60px 0 3px #535353,
    -30px 60px 0 3px #535353, -25px 60px 0 3px #535353, -20px 60px 0 3px #535353,
    -15px 60px 0 3px #535353, -10px 60px 0 3px #535353, -5px 60px 0 3px #535353,
    0px 60px 0 3px #535353, 5px 60px 0 3px #535353, 10px 60px 0 3px #535353,
    -60px 65px 0 3px #535353, -55px 65px 0 3px #535353, -50px 65px 0 3px #535353,
    -45px 65px 0 3px #535353, -40px 65px 0 3px #535353, -35px 65px 0 3px #535353,
    -30px 65px 0 3px #535353, -25px 65px 0 3px #535353, -20px 65px 0 3px #535353,
    -15px 65px 0 3px #535353, -10px 65px 0 3px #535353, -5px 65px 0 3px #535353,
    0px 65px 0 3px #535353, 5px 65px 0 3px #535353, -55px 70px 0 3px #535353,
    -50px 70px 0 3px #535353, -45px 70px 0 3px #535353, -40px 70px 0 3px #535353,
    -35px 70px 0 3px #535353, -30px 70px 0 3px #535353, -25px 70px 0 3px #535353,
    -20px 70px 0 3px #535353, -15px 70px 0 3px #535353, -10px 70px 0 3px #535353,
    -5px 70px 0 3px #535353, 0px 70px 0 3px #535353, 5px 70px 0 3px #535353,
    -50px 75px 0 3px #535353, -45px 75px 0 3px #535353, -40px 75px 0 3px #535353,
    -35px 75px 0 3px #535353, -30px 75px 0 3px #535353, -25px 75px 0 3px #535353,
    -20px 75px 0 3px #535353, -15px 75px 0 3px #535353, -10px 75px 0 3px #535353,
    -5px 75px 0 3px #535353, 0px 75px 0 3px #535353, -45px 80px 0 3px #535353,
    -40px 80px 0 3px #535353, -35px 80px 0 3px #535353, -30px 80px 0 3px #535353,
    -25px 80px 0 3px #535353, -20px 80px 0 3px #535353, -15px 80px 0 3px #535353,
    -10px 80px 0 3px #535353, -5px 80px 0 3px #535353, -40px 85px 0 3px #535353,
    -35px 85px 0 3px #535353, -20px 85px 0 3px #535353, -15px 85px 0 3px #535353,
    -35px 90px 0 3px #535353, -30px 90px 0 3px #535353, -15px 90px 0 3px #535353,
    -15px 95px 0 3px #535353, -15px 100px 0 3px #535353, -10px 100px 0 3px #535353;
}
}
@-o-keyframes run {
0%,
49.999%,
100% {
    box-shadow: 0px 0 0 3px #535353, 5px 0 0 3px #535353, 10px 0 0 3px #535353, 15px 0 0 3px #535353,
    20px 0 0 3px #535353, 25px 0 0 3px #535353, 30px 0 0 3px #535353, 35px 0 0 3px #535353,
    -5px 5px 0 3px #535353, 0px 5px 0 3px #535353, 5px 5px 0 3px #535353, 10px 5px 0 3px #535353,
    15px 5px 0 3px #535353, 20px 5px 0 3px #535353, 25px 5px 0 3px #535353, 30px 5px 0 3px #535353,
    35px 5px 0 3px #535353, 40px 5px 0 3px #535353, -5px 10px 0 3px #535353,
    0px 10px 0 3px #535353, 10px 10px 0 3px #535353, 15px 10px 0 3px #535353,
    20px 10px 0 3px #535353, 25px 10px 0 3px #535353, 30px 10px 0 3px #535353,
    35px 10px 0 3px #535353, 40px 10px 0 3px #535353, -5px 15px 0 3px #535353,
    0px 15px 0 3px #535353, 5px 15px 0 3px #535353, 10px 15px 0 3px #535353,
    15px 15px 0 3px #535353, 20px 15px 0 3px #535353, 25px 15px 0 3px #535353,
    30px 15px 0 3px #535353, 35px 15px 0 3px #535353, 40px 15px 0 3px #535353,
    -5px 20px 0 3px #535353, 0px 20px 0 3px #535353, 5px 20px 0 3px #535353,
    10px 20px 0 3px #535353, 15px 20px 0 3px #535353, 20px 20px 0 3px #535353,
    25px 20px 0 3px #535353, 30px 20px 0 3px #535353, 35px 20px 0 3px #535353,
    40px 20px 0 3px #535353, -5px 25px 0 3px #535353, 0px 25px 0 3px #535353,
    5px 25px 0 3px #535353, 10px 25px 0 3px #535353, 15px 25px 0 3px #535353,
    -5px 30px 0 3px #535353, 0px 30px 0 3px #535353, 5px 30px 0 3px #535353,
    10px 30px 0 3px #535353, 15px 30px 0 3px #535353, 20px 30px 0 3px #535353,
    25px 30px 0 3px #535353, 30px 30px 0 3px #535353, -65px 35px 0 3px #535353,
    -10px 35px 0 3px #535353, -5px 35px 0 3px #535353, 0px 35px 0 3px #535353,
    5px 35px 0 3px #535353, 10px 35px 0 3px #535353, -65px 40px 0 3px #535353,
    -20px 40px 0 3px #535353, -15px 40px 0 3px #535353, -10px 40px 0 3px #535353,
    -5px 40px 0 3px #535353, 0px 40px 0 3px #535353, 5px 40px 0 3px #535353,
    10px 40px 0 3px #535353, -65px 45px 0 3px #535353, -60px 45px 0 3px #535353,
    -30px 45px 0 3px #535353, -25px 45px 0 3px #535353, -20px 45px 0 3px #535353,
    -15px 45px 0 3px #535353, -10px 45px 0 3px #535353, -5px 45px 0 3px #535353,
    0px 45px 0 3px #535353, 5px 45px 0 3px #535353, 10px 45px 0 3px #535353,
    15px 45px 0 3px #535353, 20px 45px 0 3px #535353, -65px 50px 0 3px #535353,
    -60px 50px 0 3px #535353, -55px 50px 0 3px #535353, -35px 50px 0 3px #535353,
    -30px 50px 0 3px #535353, -25px 50px 0 3px #535353, -20px 50px 0 3px #535353,
    -15px 50px 0 3px #535353, -10px 50px 0 3px #535353, -5px 50px 0 3px #535353,
    0px 50px 0 3px #535353, 5px 50px 0 3px #535353, 10px 50px 0 3px #535353,
    20px 50px 0 3px #535353, -65px 55px 0 3px #535353, -60px 55px 0 3px #535353,
    -55px 55px 0 3px #535353, -50px 55px 0 3px #535353, -45px 55px 0 3px #535353,
    -40px 55px 0 3px #535353, -35px 55px 0 3px #535353, -30px 55px 0 3px #535353,
    -25px 55px 0 3px #535353, -20px 55px 0 3px #535353, -15px 55px 0 3px #535353,
    -10px 55px 0 3px #535353, -5px 55px 0 3px #535353, 0px 55px 0 3px #535353,
    5px 55px 0 3px #535353, 10px 55px 0 3px #535353, -65px 60px 0 3px #535353,
    -60px 60px 0 3px #535353, -55px 60px 0 3px #535353, -50px 60px 0 3px #535353,
    -45px 60px 0 3px #535353, -40px 60px 0 3px #535353, -35px 60px 0 3px #535353,
    -30px 60px 0 3px #535353, -25px 60px 0 3px #535353, -20px 60px 0 3px #535353,
    -15px 60px 0 3px #535353, -10px 60px 0 3px #535353, -5px 60px 0 3px #535353,
    0px 60px 0 3px #535353, 5px 60px 0 3px #535353, 10px 60px 0 3px #535353,
    -60px 65px 0 3px #535353, -55px 65px 0 3px #535353, -50px 65px 0 3px #535353,
    -45px 65px 0 3px #535353, -40px 65px 0 3px #535353, -35px 65px 0 3px #535353,
    -30px 65px 0 3px #535353, -25px 65px 0 3px #535353, -20px 65px 0 3px #535353,
    -15px 65px 0 3px #535353, -10px 65px 0 3px #535353, -5px 65px 0 3px #535353,
    0px 65px 0 3px #535353, 5px 65px 0 3px #535353, -55px 70px 0 3px #535353,
    -50px 70px 0 3px #535353, -45px 70px 0 3px #535353, -40px 70px 0 3px #535353,
    -35px 70px 0 3px #535353, -30px 70px 0 3px #535353, -25px 70px 0 3px #535353,
    -20px 70px 0 3px #535353, -15px 70px 0 3px #535353, -10px 70px 0 3px #535353,
    -5px 70px 0 3px #535353, 0px 70px 0 3px #535353, 5px 70px 0 3px #535353,
    -50px 75px 0 3px #535353, -45px 75px 0 3px #535353, -40px 75px 0 3px #535353,
    -35px 75px 0 3px #535353, -30px 75px 0 3px #535353, -25px 75px 0 3px #535353,
    -20px 75px 0 3px #535353, -15px 75px 0 3px #535353, -10px 75px 0 3px #535353,
    -5px 75px 0 3px #535353, 0px 75px 0 3px #535353, -45px 80px 0 3px #535353,
    -40px 80px 0 3px #535353, -35px 80px 0 3px #535353, -30px 80px 0 3px #535353,
    -25px 80px 0 3px #535353, -20px 80px 0 3px #535353, -15px 80px 0 3px #535353,
    -10px 80px 0 3px #535353, -5px 80px 0 3px #535353, -40px 85px 0 3px #535353,
    -35px 85px 0 3px #535353, -30px 85px 0 3px #535353, -20px 85px 0 3px #535353,
    -15px 85px 0 3px #535353, -40px 90px 0 3px #535353, -35px 90px 0 3px #535353,
    -15px 90px 0 3px #535353, -10px 90px 0 3px #535353, -40px 95px 0 3px #535353,
    -40px 100px 0 3px #535353, -35px 100px 0 3px #535353;
}
50%,
99.999% {
    box-shadow: 0px 0 0 3px #535353, 5px 0 0 3px #535353, 10px 0 0 3px #535353, 15px 0 0 3px #535353,
    20px 0 0 3px #535353, 25px 0 0 3px #535353, 30px 0 0 3px #535353, 35px 0 0 3px #535353,
    -5px 5px 0 3px #535353, 0px 5px 0 3px #535353, 5px 5px 0 3px #535353, 10px 5px 0 3px #535353,
    15px 5px 0 3px #535353, 20px 5px 0 3px #535353, 25px 5px 0 3px #535353, 30px 5px 0 3px #535353,
    35px 5px 0 3px #535353, 40px 5px 0 3px #535353, -5px 10px 0 3px #535353,
    0px 10px 0 3px #535353, 10px 10px 0 3px #535353, 15px 10px 0 3px #535353,
    20px 10px 0 3px #535353, 25px 10px 0 3px #535353, 30px 10px 0 3px #535353,
    35px 10px 0 3px #535353, 40px 10px 0 3px #535353, -5px 15px 0 3px #535353,
    0px 15px 0 3px #535353, 5px 15px 0 3px #535353, 10px 15px 0 3px #535353,
    15px 15px 0 3px #535353, 20px 15px 0 3px #535353, 25px 15px 0 3px #535353,
    30px 15px 0 3px #535353, 35px 15px 0 3px #535353, 40px 15px 0 3px #535353,
    -5px 20px 0 3px #535353, 0px 20px 0 3px #535353, 5px 20px 0 3px #535353,
    10px 20px 0 3px #535353, 15px 20px 0 3px #535353, 20px 20px 0 3px #535353,
    25px 20px 0 3px #535353, 30px 20px 0 3px #535353, 35px 20px 0 3px #535353,
    40px 20px 0 3px #535353, -5px 25px 0 3px #535353, 0px 25px 0 3px #535353,
    5px 25px 0 3px #535353, 10px 25px 0 3px #535353, 15px 25px 0 3px #535353,
    -5px 30px 0 3px #535353, 0px 30px 0 3px #535353, 5px 30px 0 3px #535353,
    10px 30px 0 3px #535353, 15px 30px 0 3px #535353, 20px 30px 0 3px #535353,
    25px 30px 0 3px #535353, 30px 30px 0 3px #535353, -65px 35px 0 3px #535353,
    -10px 35px 0 3px #535353, -5px 35px 0 3px #535353, 0px 35px 0 3px #535353,
    5px 35px 0 3px #535353, 10px 35px 0 3px #535353, -65px 40px 0 3px #535353,
    -20px 40px 0 3px #535353, -15px 40px 0 3px #535353, -10px 40px 0 3px #535353,
    -5px 40px 0 3px #535353, 0px 40px 0 3px #535353, 5px 40px 0 3px #535353,
    10px 40px 0 3px #535353, -65px 45px 0 3px #535353, -60px 45px 0 3px #535353,
    -30px 45px 0 3px #535353, -25px 45px 0 3px #535353, -20px 45px 0 3px #535353,
    -15px 45px 0 3px #535353, -10px 45px 0 3px #535353, -5px 45px 0 3px #535353,
    0px 45px 0 3px #535353, 5px 45px 0 3px #535353, 10px 45px 0 3px #535353,
    15px 45px 0 3px #535353, 20px 45px 0 3px #535353, -65px 50px 0 3px #535353,
    -60px 50px 0 3px #535353, -55px 50px 0 3px #535353, -35px 50px 0 3px #535353,
    -30px 50px 0 3px #535353, -25px 50px 0 3px #535353, -20px 50px 0 3px #535353,
    -15px 50px 0 3px #535353, -10px 50px 0 3px #535353, -5px 50px 0 3px #535353,
    0px 50px 0 3px #535353, 5px 50px 0 3px #535353, 10px 50px 0 3px #535353,
    20px 50px 0 3px #535353, -65px 55px 0 3px #535353, -60px 55px 0 3px #535353,
    -55px 55px 0 3px #535353, -50px 55px 0 3px #535353, -45px 55px 0 3px #535353,
    -40px 55px 0 3px #535353, -35px 55px 0 3px #535353, -30px 55px 0 3px #535353,
    -25px 55px 0 3px #535353, -20px 55px 0 3px #535353, -15px 55px 0 3px #535353,
    -10px 55px 0 3px #535353, -5px 55px 0 3px #535353, 0px 55px 0 3px #535353,
    5px 55px 0 3px #535353, 10px 55px 0 3px #535353, -65px 60px 0 3px #535353,
    -60px 60px 0 3px #535353, -55px 60px 0 3px #535353, -50px 60px 0 3px #535353,
    -45px 60px 0 3px #535353, -40px 60px 0 3px #535353, -35px 60px 0 3px #535353,
    -30px 60px 0 3px #535353, -25px 60px 0 3px #535353, -20px 60px 0 3px #535353,
    -15px 60px 0 3px #535353, -10px 60px 0 3px #535353, -5px 60px 0 3px #535353,
    0px 60px 0 3px #535353, 5px 60px 0 3px #535353, 10px 60px 0 3px #535353,
    -60px 65px 0 3px #535353, -55px 65px 0 3px #535353, -50px 65px 0 3px #535353,
    -45px 65px 0 3px #535353, -40px 65px 0 3px #535353, -35px 65px 0 3px #535353,
    -30px 65px 0 3px #535353, -25px 65px 0 3px #535353, -20px 65px 0 3px #535353,
    -15px 65px 0 3px #535353, -10px 65px 0 3px #535353, -5px 65px 0 3px #535353,
    0px 65px 0 3px #535353, 5px 65px 0 3px #535353, -55px 70px 0 3px #535353,
    -50px 70px 0 3px #535353, -45px 70px 0 3px #535353, -40px 70px 0 3px #535353,
    -35px 70px 0 3px #535353, -30px 70px 0 3px #535353, -25px 70px 0 3px #535353,
    -20px 70px 0 3px #535353, -15px 70px 0 3px #535353, -10px 70px 0 3px #535353,
    -5px 70px 0 3px #535353, 0px 70px 0 3px #535353, 5px 70px 0 3px #535353,
    -50px 75px 0 3px #535353, -45px 75px 0 3px #535353, -40px 75px 0 3px #535353,
    -35px 75px 0 3px #535353, -30px 75px 0 3px #535353, -25px 75px 0 3px #535353,
    -20px 75px 0 3px #535353, -15px 75px 0 3px #535353, -10px 75px 0 3px #535353,
    -5px 75px 0 3px #535353, 0px 75px 0 3px #535353, -45px 80px 0 3px #535353,
    -40px 80px 0 3px #535353, -35px 80px 0 3px #535353, -30px 80px 0 3px #535353,
    -25px 80px 0 3px #535353, -20px 80px 0 3px #535353, -15px 80px 0 3px #535353,
    -10px 80px 0 3px #535353, -5px 80px 0 3px #535353, -40px 85px 0 3px #535353,
    -35px 85px 0 3px #535353, -20px 85px 0 3px #535353, -15px 85px 0 3px #535353,
    -35px 90px 0 3px #535353, -30px 90px 0 3px #535353, -15px 90px 0 3px #535353,
    -15px 95px 0 3px #535353, -15px 100px 0 3px #535353, -10px 100px 0 3px #535353;
}
}
@keyframes run {
0%,
49.999%,
100% {
    box-shadow: 0px 0 0 3px #535353, 5px 0 0 3px #535353, 10px 0 0 3px #535353, 15px 0 0 3px #535353,
    20px 0 0 3px #535353, 25px 0 0 3px #535353, 30px 0 0 3px #535353, 35px 0 0 3px #535353,
    -5px 5px 0 3px #535353, 0px 5px 0 3px #535353, 5px 5px 0 3px #535353, 10px 5px 0 3px #535353,
    15px 5px 0 3px #535353, 20px 5px 0 3px #535353, 25px 5px 0 3px #535353, 30px 5px 0 3px #535353,
    35px 5px 0 3px #535353, 40px 5px 0 3px #535353, -5px 10px 0 3px #535353,
    0px 10px 0 3px #535353, 10px 10px 0 3px #535353, 15px 10px 0 3px #535353,
    20px 10px 0 3px #535353, 25px 10px 0 3px #535353, 30px 10px 0 3px #535353,
    35px 10px 0 3px #535353, 40px 10px 0 3px #535353, -5px 15px 0 3px #535353,
    0px 15px 0 3px #535353, 5px 15px 0 3px #535353, 10px 15px 0 3px #535353,
    15px 15px 0 3px #535353, 20px 15px 0 3px #535353, 25px 15px 0 3px #535353,
    30px 15px 0 3px #535353, 35px 15px 0 3px #535353, 40px 15px 0 3px #535353,
    -5px 20px 0 3px #535353, 0px 20px 0 3px #535353, 5px 20px 0 3px #535353,
    10px 20px 0 3px #535353, 15px 20px 0 3px #535353, 20px 20px 0 3px #535353,
    25px 20px 0 3px #535353, 30px 20px 0 3px #535353, 35px 20px 0 3px #535353,
    40px 20px 0 3px #535353, -5px 25px 0 3px #535353, 0px 25px 0 3px #535353,
    5px 25px 0 3px #535353, 10px 25px 0 3px #535353, 15px 25px 0 3px #535353,
    -5px 30px 0 3px #535353, 0px 30px 0 3px #535353, 5px 30px 0 3px #535353,
    10px 30px 0 3px #535353, 15px 30px 0 3px #535353, 20px 30px 0 3px #535353,
    25px 30px 0 3px #535353, 30px 30px 0 3px #535353, -65px 35px 0 3px #535353,
    -10px 35px 0 3px #535353, -5px 35px 0 3px #535353, 0px 35px 0 3px #535353,
    5px 35px 0 3px #535353, 10px 35px 0 3px #535353, -65px 40px 0 3px #535353,
    -20px 40px 0 3px #535353, -15px 40px 0 3px #535353, -10px 40px 0 3px #535353,
    -5px 40px 0 3px #535353, 0px 40px 0 3px #535353, 5px 40px 0 3px #535353,
    10px 40px 0 3px #535353, -65px 45px 0 3px #535353, -60px 45px 0 3px #535353,
    -30px 45px 0 3px #535353, -25px 45px 0 3px #535353, -20px 45px 0 3px #535353,
    -15px 45px 0 3px #535353, -10px 45px 0 3px #535353, -5px 45px 0 3px #535353,
    0px 45px 0 3px #535353, 5px 45px 0 3px #535353, 10px 45px 0 3px #535353,
    15px 45px 0 3px #535353, 20px 45px 0 3px #535353, -65px 50px 0 3px #535353,
    -60px 50px 0 3px #535353, -55px 50px 0 3px #535353, -35px 50px 0 3px #535353,
    -30px 50px 0 3px #535353, -25px 50px 0 3px #535353, -20px 50px 0 3px #535353,
    -15px 50px 0 3px #535353, -10px 50px 0 3px #535353, -5px 50px 0 3px #535353,
    0px 50px 0 3px #535353, 5px 50px 0 3px #535353, 10px 50px 0 3px #535353,
    20px 50px 0 3px #535353, -65px 55px 0 3px #535353, -60px 55px 0 3px #535353,
    -55px 55px 0 3px #535353, -50px 55px 0 3px #535353, -45px 55px 0 3px #535353,
    -40px 55px 0 3px #535353, -35px 55px 0 3px #535353, -30px 55px 0 3px #535353,
    -25px 55px 0 3px #535353, -20px 55px 0 3px #535353, -15px 55px 0 3px #535353,
    -10px 55px 0 3px #535353, -5px 55px 0 3px #535353, 0px 55px 0 3px #535353,
    5px 55px 0 3px #535353, 10px 55px 0 3px #535353, -65px 60px 0 3px #535353,
    -60px 60px 0 3px #535353, -55px 60px 0 3px #535353, -50px 60px 0 3px #535353,
    -45px 60px 0 3px #535353, -40px 60px 0 3px #535353, -35px 60px 0 3px #535353,
    -30px 60px 0 3px #535353, -25px 60px 0 3px #535353, -20px 60px 0 3px #535353,
    -15px 60px 0 3px #535353, -10px 60px 0 3px #535353, -5px 60px 0 3px #535353,
    0px 60px 0 3px #535353, 5px 60px 0 3px #535353, 10px 60px 0 3px #535353,
    -60px 65px 0 3px #535353, -55px 65px 0 3px #535353, -50px 65px 0 3px #535353,
    -45px 65px 0 3px #535353, -40px 65px 0 3px #535353, -35px 65px 0 3px #535353,
    -30px 65px 0 3px #535353, -25px 65px 0 3px #535353, -20px 65px 0 3px #535353,
    -15px 65px 0 3px #535353, -10px 65px 0 3px #535353, -5px 65px 0 3px #535353,
    0px 65px 0 3px #535353, 5px 65px 0 3px #535353, -55px 70px 0 3px #535353,
    -50px 70px 0 3px #535353, -45px 70px 0 3px #535353, -40px 70px 0 3px #535353,
    -35px 70px 0 3px #535353, -30px 70px 0 3px #535353, -25px 70px 0 3px #535353,
    -20px 70px 0 3px #535353, -15px 70px 0 3px #535353, -10px 70px 0 3px #535353,
    -5px 70px 0 3px #535353, 0px 70px 0 3px #535353, 5px 70px 0 3px #535353,
    -50px 75px 0 3px #535353, -45px 75px 0 3px #535353, -40px 75px 0 3px #535353,
    -35px 75px 0 3px #535353, -30px 75px 0 3px #535353, -25px 75px 0 3px #535353,
    -20px 75px 0 3px #535353, -15px 75px 0 3px #535353, -10px 75px 0 3px #535353,
    -5px 75px 0 3px #535353, 0px 75px 0 3px #535353, -45px 80px 0 3px #535353,
    -40px 80px 0 3px #535353, -35px 80px 0 3px #535353, -30px 80px 0 3px #535353,
    -25px 80px 0 3px #535353, -20px 80px 0 3px #535353, -15px 80px 0 3px #535353,
    -10px 80px 0 3px #535353, -5px 80px 0 3px #535353, -40px 85px 0 3px #535353,
    -35px 85px 0 3px #535353, -30px 85px 0 3px #535353, -20px 85px 0 3px #535353,
    -15px 85px 0 3px #535353, -40px 90px 0 3px #535353, -35px 90px 0 3px #535353,
    -15px 90px 0 3px #535353, -10px 90px 0 3px #535353, -40px 95px 0 3px #535353,
    -40px 100px 0 3px #535353, -35px 100px 0 3px #535353;
}
50%,
99.999% {
    box-shadow: 0px 0 0 3px #535353, 5px 0 0 3px #535353, 10px 0 0 3px #535353, 15px 0 0 3px #535353,
    20px 0 0 3px #535353, 25px 0 0 3px #535353, 30px 0 0 3px #535353, 35px 0 0 3px #535353,
    -5px 5px 0 3px #535353, 0px 5px 0 3px #535353, 5px 5px 0 3px #535353, 10px 5px 0 3px #535353,
    15px 5px 0 3px #535353, 20px 5px 0 3px #535353, 25px 5px 0 3px #535353, 30px 5px 0 3px #535353,
    35px 5px 0 3px #535353, 40px 5px 0 3px #535353, -5px 10px 0 3px #535353,
    0px 10px 0 3px #535353, 10px 10px 0 3px #535353, 15px 10px 0 3px #535353,
    20px 10px 0 3px #535353, 25px 10px 0 3px #535353, 30px 10px 0 3px #535353,
    35px 10px 0 3px #535353, 40px 10px 0 3px #535353, -5px 15px 0 3px #535353,
    0px 15px 0 3px #535353, 5px 15px 0 3px #535353, 10px 15px 0 3px #535353,
    15px 15px 0 3px #535353, 20px 15px 0 3px #535353, 25px 15px 0 3px #535353,
    30px 15px 0 3px #535353, 35px 15px 0 3px #535353, 40px 15px 0 3px #535353,
    -5px 20px 0 3px #535353, 0px 20px 0 3px #535353, 5px 20px 0 3px #535353,
    10px 20px 0 3px #535353, 15px 20px 0 3px #535353, 20px 20px 0 3px #535353,
    25px 20px 0 3px #535353, 30px 20px 0 3px #535353, 35px 20px 0 3px #535353,
    40px 20px 0 3px #535353, -5px 25px 0 3px #535353, 0px 25px 0 3px #535353,
    5px 25px 0 3px #535353, 10px 25px 0 3px #535353, 15px 25px 0 3px #535353,
    -5px 30px 0 3px #535353, 0px 30px 0 3px #535353, 5px 30px 0 3px #535353,
    10px 30px 0 3px #535353, 15px 30px 0 3px #535353, 20px 30px 0 3px #535353,
    25px 30px 0 3px #535353, 30px 30px 0 3px #535353, -65px 35px 0 3px #535353,
    -10px 35px 0 3px #535353, -5px 35px 0 3px #535353, 0px 35px 0 3px #535353,
    5px 35px 0 3px #535353, 10px 35px 0 3px #535353, -65px 40px 0 3px #535353,
    -20px 40px 0 3px #535353, -15px 40px 0 3px #535353, -10px 40px 0 3px #535353,
    -5px 40px 0 3px #535353, 0px 40px 0 3px #535353, 5px 40px 0 3px #535353,
    10px 40px 0 3px #535353, -65px 45px 0 3px #535353, -60px 45px 0 3px #535353,
    -30px 45px 0 3px #535353, -25px 45px 0 3px #535353, -20px 45px 0 3px #535353,
    -15px 45px 0 3px #535353, -10px 45px 0 3px #535353, -5px 45px 0 3px #535353,
    0px 45px 0 3px #535353, 5px 45px 0 3px #535353, 10px 45px 0 3px #535353,
    15px 45px 0 3px #535353, 20px 45px 0 3px #535353, -65px 50px 0 3px #535353,
    -60px 50px 0 3px #535353, -55px 50px 0 3px #535353, -35px 50px 0 3px #535353,
    -30px 50px 0 3px #535353, -25px 50px 0 3px #535353, -20px 50px 0 3px #535353,
    -15px 50px 0 3px #535353, -10px 50px 0 3px #535353, -5px 50px 0 3px #535353,
    0px 50px 0 3px #535353, 5px 50px 0 3px #535353, 10px 50px 0 3px #535353,
    20px 50px 0 3px #535353, -65px 55px 0 3px #535353, -60px 55px 0 3px #535353,
    -55px 55px 0 3px #535353, -50px 55px 0 3px #535353, -45px 55px 0 3px #535353,
    -40px 55px 0 3px #535353, -35px 55px 0 3px #535353, -30px 55px 0 3px #535353,
    -25px 55px 0 3px #535353, -20px 55px 0 3px #535353, -15px 55px 0 3px #535353,
    -10px 55px 0 3px #535353, -5px 55px 0 3px #535353, 0px 55px 0 3px #535353,
    5px 55px 0 3px #535353, 10px 55px 0 3px #535353, -65px 60px 0 3px #535353,
    -60px 60px 0 3px #535353, -55px 60px 0 3px #535353, -50px 60px 0 3px #535353,
    -45px 60px 0 3px #535353, -40px 60px 0 3px #535353, -35px 60px 0 3px #535353,
    -30px 60px 0 3px #535353, -25px 60px 0 3px #535353, -20px 60px 0 3px #535353,
    -15px 60px 0 3px #535353, -10px 60px 0 3px #535353, -5px 60px 0 3px #535353,
    0px 60px 0 3px #535353, 5px 60px 0 3px #535353, 10px 60px 0 3px #535353,
    -60px 65px 0 3px #535353, -55px 65px 0 3px #535353, -50px 65px 0 3px #535353,
    -45px 65px 0 3px #535353, -40px 65px 0 3px #535353, -35px 65px 0 3px #535353,
    -30px 65px 0 3px #535353, -25px 65px 0 3px #535353, -20px 65px 0 3px #535353,
    -15px 65px 0 3px #535353, -10px 65px 0 3px #535353, -5px 65px 0 3px #535353,
    0px 65px 0 3px #535353, 5px 65px 0 3px #535353, -55px 70px 0 3px #535353,
    -50px 70px 0 3px #535353, -45px 70px 0 3px #535353, -40px 70px 0 3px #535353,
    -35px 70px 0 3px #535353, -30px 70px 0 3px #535353, -25px 70px 0 3px #535353,
    -20px 70px 0 3px #535353, -15px 70px 0 3px #535353, -10px 70px 0 3px #535353,
    -5px 70px 0 3px #535353, 0px 70px 0 3px #535353, 5px 70px 0 3px #535353,
    -50px 75px 0 3px #535353, -45px 75px 0 3px #535353, -40px 75px 0 3px #535353,
    -35px 75px 0 3px #535353, -30px 75px 0 3px #535353, -25px 75px 0 3px #535353,
    -20px 75px 0 3px #535353, -15px 75px 0 3px #535353, -10px 75px 0 3px #535353,
    -5px 75px 0 3px #535353, 0px 75px 0 3px #535353, -45px 80px 0 3px #535353,
    -40px 80px 0 3px #535353, -35px 80px 0 3px #535353, -30px 80px 0 3px #535353,
    -25px 80px 0 3px #535353, -20px 80px 0 3px #535353, -15px 80px 0 3px #535353,
    -10px 80px 0 3px #535353, -5px 80px 0 3px #535353, -40px 85px 0 3px #535353,
    -35px 85px 0 3px #535353, -20px 85px 0 3px #535353, -15px 85px 0 3px #535353,
    -35px 90px 0 3px #535353, -30px 90px 0 3px #535353, -15px 90px 0 3px #535353,
    -15px 95px 0 3px #535353, -15px 100px 0 3px #535353, -10px 100px 0 3px #535353;
}
}
@-webkit-keyframes ptero {
0%,
49.999%,
100% {
    box-shadow: 0px 85px 0 3px #535353, 5px 85px 0 3px #535353, -5px 90px 0 3px #535353,
    0px 90px 0 3px #535353, 5px 90px 0 3px #535353, -10px 95px 0 3px #535353,
    -5px 95px 0 3px #535353, 0px 95px 0 3px #535353, 5px 95px 0 3px #535353,
    10px 95px 0 3px #535353, -15px 100px 0 3px #535353, -10px 100px 0 3px #535353,
    -5px 100px 0 3px #535353, 0px 100px 0 3px #535353, 5px 100px 0 3px #535353,
    10px 100px 0 3px #535353, -20px 105px 0 3px #535353, -15px 105px 0 3px #535353,
    -10px 105px 0 3px #535353, -5px 105px 0 3px #535353, 0px 105px 0 3px #535353,
    5px 105px 0 3px #535353, 10px 105px 0 3px #535353, 15px 105px 0 3px #535353,
    20px 105px 0 3px #535353, 25px 105px 0 3px #535353, 30px 105px 0 3px #535353,
    35px 105px 0 3px #535353, 10px 110px 0 3px #535353, 15px 110px 0 3px #535353,
    20px 110px 0 3px #535353, 25px 110px 0 3px #535353, 30px 110px 0 3px #535353,
    35px 110px 0 3px #535353, 40px 110px 0 3px #535353, 15px 115px 0 3px #535353,
    20px 115px 0 3px #535353, 25px 115px 0 3px #535353, 30px 115px 0 3px #535353,
    35px 115px 0 3px #535353, 40px 115px 0 3px #535353, 45px 115px 0 3px #535353,
    50px 115px 0 3px #535353, 55px 115px 0 3px #535353, 60px 115px 0 3px #535353,
    65px 115px 0 3px #535353, 70px 115px 0 3px #535353, 75px 115px 0 3px #535353,
    15px 120px 0 3px #535353, 20px 120px 0 3px #535353, 25px 120px 0 3px #535353,
    30px 120px 0 3px #535353, 35px 120px 0 3px #535353, 40px 120px 0 3px #535353,
    45px 120px 0 3px #535353, 50px 120px 0 3px #535353, 55px 120px 0 3px #535353,
    60px 120px 0 3px #535353, 15px 125px 0 3px #535353, 20px 125px 0 3px #535353,
    25px 125px 0 3px #535353, 30px 125px 0 3px #535353, 35px 125px 0 3px #535353,
    40px 125px 0 3px #535353, 45px 125px 0 3px #535353, 50px 125px 0 3px #535353,
    55px 125px 0 3px #535353, 60px 125px 0 3px #535353, 65px 125px 0 3px #535353,
    70px 125px 0 3px #535353, 15px 130px 0 3px #535353, 20px 130px 0 3px #535353,
    25px 130px 0 3px #535353, 30px 130px 0 3px #535353, 35px 130px 0 3px #535353,
    40px 130px 0 3px #535353, 45px 130px 0 3px #535353, 50px 130px 0 3px #535353,
    55px 130px 0 3px #535353, 15px 135px 0 3px #535353, 20px 135px 0 3px #535353,
    25px 135px 0 3px #535353, 30px 135px 0 3px #535353, 15px 140px 0 3px #535353,
    20px 140px 0 3px #535353, 25px 140px 0 3px #535353, 15px 145px 0 3px #535353,
    20px 145px 0 3px #535353, 15px 150px 0 3px #535353, 20px 150px 0 3px #535353,
    15px 155px 0 3px #535353;
}
50%,
99.999% {
    box-shadow: 0px 85px 0 3px #535353, 5px 85px 0 3px #535353, -5px 90px 0 3px #535353,
    0px 90px 0 3px #535353, 5px 90px 0 3px #535353, -10px 95px 0 3px #535353,
    -5px 95px 0 3px #535353, 0px 95px 0 3px #535353, 5px 95px 0 3px #535353,
    10px 95px 0 3px #535353, -15px 100px 0 3px #535353, -10px 100px 0 3px #535353,
    -5px 100px 0 3px #535353, 0px 100px 0 3px #535353, 5px 100px 0 3px #535353,
    10px 100px 0 3px #535353, -20px 105px 0 3px #535353, -15px 105px 0 3px #535353,
    -10px 105px 0 3px #535353, -5px 105px 0 3px #535353, 0px 105px 0 3px #535353,
    5px 105px 0 3px #535353, 10px 105px 0 3px #535353, 15px 105px 0 3px #535353,
    20px 105px 0 3px #535353, 25px 105px 0 3px #535353, 30px 105px 0 3px #535353,
    35px 105px 0 3px #535353, 10px 110px 0 3px #535353, 15px 110px 0 3px #535353,
    20px 110px 0 3px #535353, 25px 110px 0 3px #535353, 30px 110px 0 3px #535353,
    35px 110px 0 3px #535353, 40px 110px 0 3px #535353, 15px 115px 0 3px #535353,
    20px 115px 0 3px #535353, 25px 115px 0 3px #535353, 30px 115px 0 3px #535353,
    35px 115px 0 3px #535353, 40px 115px 0 3px #535353, 45px 115px 0 3px #535353,
    50px 115px 0 3px #535353, 55px 115px 0 3px #535353, 60px 115px 0 3px #535353,
    65px 115px 0 3px #535353, 70px 115px 0 3px #535353, 75px 115px 0 3px #535353,
    20px 120px 0 3px #535353, 25px 120px 0 3px #535353, 30px 120px 0 3px #535353,
    35px 120px 0 3px #535353, 40px 120px 0 3px #535353, 45px 120px 0 3px #535353,
    50px 120px 0 3px #535353, 55px 120px 0 3px #535353, 60px 120px 0 3px #535353,
    25px 125px 0 3px #535353, 30px 125px 0 3px #535353, 35px 125px 0 3px #535353,
    40px 125px 0 3px #535353, 45px 125px 0 3px #535353, 50px 125px 0 3px #535353,
    55px 125px 0 3px #535353, 60px 125px 0 3px #535353, 65px 125px 0 3px #535353,
    70px 125px 0 3px #535353, 30px 130px 0 3px #535353, 35px 130px 0 3px #535353,
    40px 130px 0 3px #535353, 45px 130px 0 3px #535353, 50px 130px 0 3px #535353,
    55px 130px 0 3px #535353, 20px 70px 0 3px #535353, 20px 75px 0 3px #535353,
    25px 75px 0 3px #535353, 20px 80px 0 3px #535353, 25px 80px 0 3px #535353,
    30px 80px 0 3px #535353, 25px 85px 0 3px #535353, 30px 85px 0 3px #535353,
    35px 85px 0 3px #535353, 25px 90px 0 3px #535353, 30px 90px 0 3px #535353,
    35px 90px 0 3px #535353, 40px 90px 0 3px #535353, 25px 95px 0 3px #535353,
    30px 95px 0 3px #535353, 35px 95px 0 3px #535353, 40px 95px 0 3px #535353,
    45px 95px 0 3px #535353, 25px 100px 0 3px #535353, 30px 100px 0 3px #535353,
    35px 100px 0 3px #535353, 40px 100px 0 3px #535353, 45px 100px 0 3px #535353,
    50px 100px 0 3px #535353, 40px 105px 0 3px #535353, 45px 105px 0 3px #535353,
    50px 105px 0 3px #535353, 45px 110px 0 3px #535353, 50px 110px 0 3px #535353,
    55px 110px 0 3px #535353;
}
}
@-moz-keyframes ptero {
0%,
49.999%,
100% {
    box-shadow: 0px 85px 0 3px #535353, 5px 85px 0 3px #535353, -5px 90px 0 3px #535353,
    0px 90px 0 3px #535353, 5px 90px 0 3px #535353, -10px 95px 0 3px #535353,
    -5px 95px 0 3px #535353, 0px 95px 0 3px #535353, 5px 95px 0 3px #535353,
    10px 95px 0 3px #535353, -15px 100px 0 3px #535353, -10px 100px 0 3px #535353,
    -5px 100px 0 3px #535353, 0px 100px 0 3px #535353, 5px 100px 0 3px #535353,
    10px 100px 0 3px #535353, -20px 105px 0 3px #535353, -15px 105px 0 3px #535353,
    -10px 105px 0 3px #535353, -5px 105px 0 3px #535353, 0px 105px 0 3px #535353,
    5px 105px 0 3px #535353, 10px 105px 0 3px #535353, 15px 105px 0 3px #535353,
    20px 105px 0 3px #535353, 25px 105px 0 3px #535353, 30px 105px 0 3px #535353,
    35px 105px 0 3px #535353, 10px 110px 0 3px #535353, 15px 110px 0 3px #535353,
    20px 110px 0 3px #535353, 25px 110px 0 3px #535353, 30px 110px 0 3px #535353,
    35px 110px 0 3px #535353, 40px 110px 0 3px #535353, 15px 115px 0 3px #535353,
    20px 115px 0 3px #535353, 25px 115px 0 3px #535353, 30px 115px 0 3px #535353,
    35px 115px 0 3px #535353, 40px 115px 0 3px #535353, 45px 115px 0 3px #535353,
    50px 115px 0 3px #535353, 55px 115px 0 3px #535353, 60px 115px 0 3px #535353,
    65px 115px 0 3px #535353, 70px 115px 0 3px #535353, 75px 115px 0 3px #535353,
    15px 120px 0 3px #535353, 20px 120px 0 3px #535353, 25px 120px 0 3px #535353,
    30px 120px 0 3px #535353, 35px 120px 0 3px #535353, 40px 120px 0 3px #535353,
    45px 120px 0 3px #535353, 50px 120px 0 3px #535353, 55px 120px 0 3px #535353,
    60px 120px 0 3px #535353, 15px 125px 0 3px #535353, 20px 125px 0 3px #535353,
    25px 125px 0 3px #535353, 30px 125px 0 3px #535353, 35px 125px 0 3px #535353,
    40px 125px 0 3px #535353, 45px 125px 0 3px #535353, 50px 125px 0 3px #535353,
    55px 125px 0 3px #535353, 60px 125px 0 3px #535353, 65px 125px 0 3px #535353,
    70px 125px 0 3px #535353, 15px 130px 0 3px #535353, 20px 130px 0 3px #535353,
    25px 130px 0 3px #535353, 30px 130px 0 3px #535353, 35px 130px 0 3px #535353,
    40px 130px 0 3px #535353, 45px 130px 0 3px #535353, 50px 130px 0 3px #535353,
    55px 130px 0 3px #535353, 15px 135px 0 3px #535353, 20px 135px 0 3px #535353,
    25px 135px 0 3px #535353, 30px 135px 0 3px #535353, 15px 140px 0 3px #535353,
    20px 140px 0 3px #535353, 25px 140px 0 3px #535353, 15px 145px 0 3px #535353,
    20px 145px 0 3px #535353, 15px 150px 0 3px #535353, 20px 150px 0 3px #535353,
    15px 155px 0 3px #535353;
}
50%,
99.999% {
    box-shadow: 0px 85px 0 3px #535353, 5px 85px 0 3px #535353, -5px 90px 0 3px #535353,
    0px 90px 0 3px #535353, 5px 90px 0 3px #535353, -10px 95px 0 3px #535353,
    -5px 95px 0 3px #535353, 0px 95px 0 3px #535353, 5px 95px 0 3px #535353,
    10px 95px 0 3px #535353, -15px 100px 0 3px #535353, -10px 100px 0 3px #535353,
    -5px 100px 0 3px #535353, 0px 100px 0 3px #535353, 5px 100px 0 3px #535353,
    10px 100px 0 3px #535353, -20px 105px 0 3px #535353, -15px 105px 0 3px #535353,
    -10px 105px 0 3px #535353, -5px 105px 0 3px #535353, 0px 105px 0 3px #535353,
    5px 105px 0 3px #535353, 10px 105px 0 3px #535353, 15px 105px 0 3px #535353,
    20px 105px 0 3px #535353, 25px 105px 0 3px #535353, 30px 105px 0 3px #535353,
    35px 105px 0 3px #535353, 10px 110px 0 3px #535353, 15px 110px 0 3px #535353,
    20px 110px 0 3px #535353, 25px 110px 0 3px #535353, 30px 110px 0 3px #535353,
    35px 110px 0 3px #535353, 40px 110px 0 3px #535353, 15px 115px 0 3px #535353,
    20px 115px 0 3px #535353, 25px 115px 0 3px #535353, 30px 115px 0 3px #535353,
    35px 115px 0 3px #535353, 40px 115px 0 3px #535353, 45px 115px 0 3px #535353,
    50px 115px 0 3px #535353, 55px 115px 0 3px #535353, 60px 115px 0 3px #535353,
    65px 115px 0 3px #535353, 70px 115px 0 3px #535353, 75px 115px 0 3px #535353,
    20px 120px 0 3px #535353, 25px 120px 0 3px #535353, 30px 120px 0 3px #535353,
    35px 120px 0 3px #535353, 40px 120px 0 3px #535353, 45px 120px 0 3px #535353,
    50px 120px 0 3px #535353, 55px 120px 0 3px #535353, 60px 120px 0 3px #535353,
    25px 125px 0 3px #535353, 30px 125px 0 3px #535353, 35px 125px 0 3px #535353,
    40px 125px 0 3px #535353, 45px 125px 0 3px #535353, 50px 125px 0 3px #535353,
    55px 125px 0 3px #535353, 60px 125px 0 3px #535353, 65px 125px 0 3px #535353,
    70px 125px 0 3px #535353, 30px 130px 0 3px #535353, 35px 130px 0 3px #535353,
    40px 130px 0 3px #535353, 45px 130px 0 3px #535353, 50px 130px 0 3px #535353,
    55px 130px 0 3px #535353, 20px 70px 0 3px #535353, 20px 75px 0 3px #535353,
    25px 75px 0 3px #535353, 20px 80px 0 3px #535353, 25px 80px 0 3px #535353,
    30px 80px 0 3px #535353, 25px 85px 0 3px #535353, 30px 85px 0 3px #535353,
    35px 85px 0 3px #535353, 25px 90px 0 3px #535353, 30px 90px 0 3px #535353,
    35px 90px 0 3px #535353, 40px 90px 0 3px #535353, 25px 95px 0 3px #535353,
    30px 95px 0 3px #535353, 35px 95px 0 3px #535353, 40px 95px 0 3px #535353,
    45px 95px 0 3px #535353, 25px 100px 0 3px #535353, 30px 100px 0 3px #535353,
    35px 100px 0 3px #535353, 40px 100px 0 3px #535353, 45px 100px 0 3px #535353,
    50px 100px 0 3px #535353, 40px 105px 0 3px #535353, 45px 105px 0 3px #535353,
    50px 105px 0 3px #535353, 45px 110px 0 3px #535353, 50px 110px 0 3px #535353,
    55px 110px 0 3px #535353;
}
}
@-o-keyframes ptero {
0%,
49.999%,
100% {
    box-shadow: 0px 85px 0 3px #535353, 5px 85px 0 3px #535353, -5px 90px 0 3px #535353,
    0px 90px 0 3px #535353, 5px 90px 0 3px #535353, -10px 95px 0 3px #535353,
    -5px 95px 0 3px #535353, 0px 95px 0 3px #535353, 5px 95px 0 3px #535353,
    10px 95px 0 3px #535353, -15px 100px 0 3px #535353, -10px 100px 0 3px #535353,
    -5px 100px 0 3px #535353, 0px 100px 0 3px #535353, 5px 100px 0 3px #535353,
    10px 100px 0 3px #535353, -20px 105px 0 3px #535353, -15px 105px 0 3px #535353,
    -10px 105px 0 3px #535353, -5px 105px 0 3px #535353, 0px 105px 0 3px #535353,
    5px 105px 0 3px #535353, 10px 105px 0 3px #535353, 15px 105px 0 3px #535353,
    20px 105px 0 3px #535353, 25px 105px 0 3px #535353, 30px 105px 0 3px #535353,
    35px 105px 0 3px #535353, 10px 110px 0 3px #535353, 15px 110px 0 3px #535353,
    20px 110px 0 3px #535353, 25px 110px 0 3px #535353, 30px 110px 0 3px #535353,
    35px 110px 0 3px #535353, 40px 110px 0 3px #535353, 15px 115px 0 3px #535353,
    20px 115px 0 3px #535353, 25px 115px 0 3px #535353, 30px 115px 0 3px #535353,
    35px 115px 0 3px #535353, 40px 115px 0 3px #535353, 45px 115px 0 3px #535353,
    50px 115px 0 3px #535353, 55px 115px 0 3px #535353, 60px 115px 0 3px #535353,
    65px 115px 0 3px #535353, 70px 115px 0 3px #535353, 75px 115px 0 3px #535353,
    15px 120px 0 3px #535353, 20px 120px 0 3px #535353, 25px 120px 0 3px #535353,
    30px 120px 0 3px #535353, 35px 120px 0 3px #535353, 40px 120px 0 3px #535353,
    45px 120px 0 3px #535353, 50px 120px 0 3px #535353, 55px 120px 0 3px #535353,
    60px 120px 0 3px #535353, 15px 125px 0 3px #535353, 20px 125px 0 3px #535353,
    25px 125px 0 3px #535353, 30px 125px 0 3px #535353, 35px 125px 0 3px #535353,
    40px 125px 0 3px #535353, 45px 125px 0 3px #535353, 50px 125px 0 3px #535353,
    55px 125px 0 3px #535353, 60px 125px 0 3px #535353, 65px 125px 0 3px #535353,
    70px 125px 0 3px #535353, 15px 130px 0 3px #535353, 20px 130px 0 3px #535353,
    25px 130px 0 3px #535353, 30px 130px 0 3px #535353, 35px 130px 0 3px #535353,
    40px 130px 0 3px #535353, 45px 130px 0 3px #535353, 50px 130px 0 3px #535353,
    55px 130px 0 3px #535353, 15px 135px 0 3px #535353, 20px 135px 0 3px #535353,
    25px 135px 0 3px #535353, 30px 135px 0 3px #535353, 15px 140px 0 3px #535353,
    20px 140px 0 3px #535353, 25px 140px 0 3px #535353, 15px 145px 0 3px #535353,
    20px 145px 0 3px #535353, 15px 150px 0 3px #535353, 20px 150px 0 3px #535353,
    15px 155px 0 3px #535353;
}
50%,
99.999% {
    box-shadow: 0px 85px 0 3px #535353, 5px 85px 0 3px #535353, -5px 90px 0 3px #535353,
    0px 90px 0 3px #535353, 5px 90px 0 3px #535353, -10px 95px 0 3px #535353,
    -5px 95px 0 3px #535353, 0px 95px 0 3px #535353, 5px 95px 0 3px #535353,
    10px 95px 0 3px #535353, -15px 100px 0 3px #535353, -10px 100px 0 3px #535353,
    -5px 100px 0 3px #535353, 0px 100px 0 3px #535353, 5px 100px 0 3px #535353,
    10px 100px 0 3px #535353, -20px 105px 0 3px #535353, -15px 105px 0 3px #535353,
    -10px 105px 0 3px #535353, -5px 105px 0 3px #535353, 0px 105px 0 3px #535353,
    5px 105px 0 3px #535353, 10px 105px 0 3px #535353, 15px 105px 0 3px #535353,
    20px 105px 0 3px #535353, 25px 105px 0 3px #535353, 30px 105px 0 3px #535353,
    35px 105px 0 3px #535353, 10px 110px 0 3px #535353, 15px 110px 0 3px #535353,
    20px 110px 0 3px #535353, 25px 110px 0 3px #535353, 30px 110px 0 3px #535353,
    35px 110px 0 3px #535353, 40px 110px 0 3px #535353, 15px 115px 0 3px #535353,
    20px 115px 0 3px #535353, 25px 115px 0 3px #535353, 30px 115px 0 3px #535353,
    35px 115px 0 3px #535353, 40px 115px 0 3px #535353, 45px 115px 0 3px #535353,
    50px 115px 0 3px #535353, 55px 115px 0 3px #535353, 60px 115px 0 3px #535353,
    65px 115px 0 3px #535353, 70px 115px 0 3px #535353, 75px 115px 0 3px #535353,
    20px 120px 0 3px #535353, 25px 120px 0 3px #535353, 30px 120px 0 3px #535353,
    35px 120px 0 3px #535353, 40px 120px 0 3px #535353, 45px 120px 0 3px #535353,
    50px 120px 0 3px #535353, 55px 120px 0 3px #535353, 60px 120px 0 3px #535353,
    25px 125px 0 3px #535353, 30px 125px 0 3px #535353, 35px 125px 0 3px #535353,
    40px 125px 0 3px #535353, 45px 125px 0 3px #535353, 50px 125px 0 3px #535353,
    55px 125px 0 3px #535353, 60px 125px 0 3px #535353, 65px 125px 0 3px #535353,
    70px 125px 0 3px #535353, 30px 130px 0 3px #535353, 35px 130px 0 3px #535353,
    40px 130px 0 3px #535353, 45px 130px 0 3px #535353, 50px 130px 0 3px #535353,
    55px 130px 0 3px #535353, 20px 70px 0 3px #535353, 20px 75px 0 3px #535353,
    25px 75px 0 3px #535353, 20px 80px 0 3px #535353, 25px 80px 0 3px #535353,
    30px 80px 0 3px #535353, 25px 85px 0 3px #535353, 30px 85px 0 3px #535353,
    35px 85px 0 3px #535353, 25px 90px 0 3px #535353, 30px 90px 0 3px #535353,
    35px 90px 0 3px #535353, 40px 90px 0 3px #535353, 25px 95px 0 3px #535353,
    30px 95px 0 3px #535353, 35px 95px 0 3px #535353, 40px 95px 0 3px #535353,
    45px 95px 0 3px #535353, 25px 100px 0 3px #535353, 30px 100px 0 3px #535353,
    35px 100px 0 3px #535353, 40px 100px 0 3px #535353, 45px 100px 0 3px #535353,
    50px 100px 0 3px #535353, 40px 105px 0 3px #535353, 45px 105px 0 3px #535353,
    50px 105px 0 3px #535353, 45px 110px 0 3px #535353, 50px 110px 0 3px #535353,
    55px 110px 0 3px #535353;
}
}
@keyframes ptero {
0%,
49.999%,
100% {
    box-shadow: 0px 85px 0 3px #535353, 5px 85px 0 3px #535353, -5px 90px 0 3px #535353,
    0px 90px 0 3px #535353, 5px 90px 0 3px #535353, -10px 95px 0 3px #535353,
    -5px 95px 0 3px #535353, 0px 95px 0 3px #535353, 5px 95px 0 3px #535353,
    10px 95px 0 3px #535353, -15px 100px 0 3px #535353, -10px 100px 0 3px #535353,
    -5px 100px 0 3px #535353, 0px 100px 0 3px #535353, 5px 100px 0 3px #535353,
    10px 100px 0 3px #535353, -20px 105px 0 3px #535353, -15px 105px 0 3px #535353,
    -10px 105px 0 3px #535353, -5px 105px 0 3px #535353, 0px 105px 0 3px #535353,
    5px 105px 0 3px #535353, 10px 105px 0 3px #535353, 15px 105px 0 3px #535353,
    20px 105px 0 3px #535353, 25px 105px 0 3px #535353, 30px 105px 0 3px #535353,
    35px 105px 0 3px #535353, 10px 110px 0 3px #535353, 15px 110px 0 3px #535353,
    20px 110px 0 3px #535353, 25px 110px 0 3px #535353, 30px 110px 0 3px #535353,
    35px 110px 0 3px #535353, 40px 110px 0 3px #535353, 15px 115px 0 3px #535353,
    20px 115px 0 3px #535353, 25px 115px 0 3px #535353, 30px 115px 0 3px #535353,
    35px 115px 0 3px #535353, 40px 115px 0 3px #535353, 45px 115px 0 3px #535353,
    50px 115px 0 3px #535353, 55px 115px 0 3px #535353, 60px 115px 0 3px #535353,
    65px 115px 0 3px #535353, 70px 115px 0 3px #535353, 75px 115px 0 3px #535353,
    15px 120px 0 3px #535353, 20px 120px 0 3px #535353, 25px 120px 0 3px #535353,
    30px 120px 0 3px #535353, 35px 120px 0 3px #535353, 40px 120px 0 3px #535353,
    45px 120px 0 3px #535353, 50px 120px 0 3px #535353, 55px 120px 0 3px #535353,
    60px 120px 0 3px #535353, 15px 125px 0 3px #535353, 20px 125px 0 3px #535353,
    25px 125px 0 3px #535353, 30px 125px 0 3px #535353, 35px 125px 0 3px #535353,
    40px 125px 0 3px #535353, 45px 125px 0 3px #535353, 50px 125px 0 3px #535353,
    55px 125px 0 3px #535353, 60px 125px 0 3px #535353, 65px 125px 0 3px #535353,
    70px 125px 0 3px #535353, 15px 130px 0 3px #535353, 20px 130px 0 3px #535353,
    25px 130px 0 3px #535353, 30px 130px 0 3px #535353, 35px 130px 0 3px #535353,
    40px 130px 0 3px #535353, 45px 130px 0 3px #535353, 50px 130px 0 3px #535353,
    55px 130px 0 3px #535353, 15px 135px 0 3px #535353, 20px 135px 0 3px #535353,
    25px 135px 0 3px #535353, 30px 135px 0 3px #535353, 15px 140px 0 3px #535353,
    20px 140px 0 3px #535353, 25px 140px 0 3px #535353, 15px 145px 0 3px #535353,
    20px 145px 0 3px #535353, 15px 150px 0 3px #535353, 20px 150px 0 3px #535353,
    15px 155px 0 3px #535353;
}
50%,
99.999% {
    box-shadow: 0px 85px 0 3px #535353, 5px 85px 0 3px #535353, -5px 90px 0 3px #535353,
    0px 90px 0 3px #535353, 5px 90px 0 3px #535353, -10px 95px 0 3px #535353,
    -5px 95px 0 3px #535353, 0px 95px 0 3px #535353, 5px 95px 0 3px #535353,
    10px 95px 0 3px #535353, -15px 100px 0 3px #535353, -10px 100px 0 3px #535353,
    -5px 100px 0 3px #535353, 0px 100px 0 3px #535353, 5px 100px 0 3px #535353,
    10px 100px 0 3px #535353, -20px 105px 0 3px #535353, -15px 105px 0 3px #535353,
    -10px 105px 0 3px #535353, -5px 105px 0 3px #535353, 0px 105px 0 3px #535353,
    5px 105px 0 3px #535353, 10px 105px 0 3px #535353, 15px 105px 0 3px #535353,
    20px 105px 0 3px #535353, 25px 105px 0 3px #535353, 30px 105px 0 3px #535353,
    35px 105px 0 3px #535353, 10px 110px 0 3px #535353, 15px 110px 0 3px #535353,
    20px 110px 0 3px #535353, 25px 110px 0 3px #535353, 30px 110px 0 3px #535353,
    35px 110px 0 3px #535353, 40px 110px 0 3px #535353, 15px 115px 0 3px #535353,
    20px 115px 0 3px #535353, 25px 115px 0 3px #535353, 30px 115px 0 3px #535353,
    35px 115px 0 3px #535353, 40px 115px 0 3px #535353, 45px 115px 0 3px #535353,
    50px 115px 0 3px #535353, 55px 115px 0 3px #535353, 60px 115px 0 3px #535353,
    65px 115px 0 3px #535353, 70px 115px 0 3px #535353, 75px 115px 0 3px #535353,
    20px 120px 0 3px #535353, 25px 120px 0 3px #535353, 30px 120px 0 3px #535353,
    35px 120px 0 3px #535353, 40px 120px 0 3px #535353, 45px 120px 0 3px #535353,
    50px 120px 0 3px #535353, 55px 120px 0 3px #535353, 60px 120px 0 3px #535353,
    25px 125px 0 3px #535353, 30px 125px 0 3px #535353, 35px 125px 0 3px #535353,
    40px 125px 0 3px #535353, 45px 125px 0 3px #535353, 50px 125px 0 3px #535353,
    55px 125px 0 3px #535353, 60px 125px 0 3px #535353, 65px 125px 0 3px #535353,
    70px 125px 0 3px #535353, 30px 130px 0 3px #535353, 35px 130px 0 3px #535353,
    40px 130px 0 3px #535353, 45px 130px 0 3px #535353, 50px 130px 0 3px #535353,
    55px 130px 0 3px #535353, 20px 70px 0 3px #535353, 20px 75px 0 3px #535353,
    25px 75px 0 3px #535353, 20px 80px 0 3px #535353, 25px 80px 0 3px #535353,
    30px 80px 0 3px #535353, 25px 85px 0 3px #535353, 30px 85px 0 3px #535353,
    35px 85px 0 3px #535353, 25px 90px 0 3px #535353, 30px 90px 0 3px #535353,
    35px 90px 0 3px #535353, 40px 90px 0 3px #535353, 25px 95px 0 3px #535353,
    30px 95px 0 3px #535353, 35px 95px 0 3px #535353, 40px 95px 0 3px #535353,
    45px 95px 0 3px #535353, 25px 100px 0 3px #535353, 30px 100px 0 3px #535353,
    35px 100px 0 3px #535353, 40px 100px 0 3px #535353, 45px 100px 0 3px #535353,
    50px 100px 0 3px #535353, 40px 105px 0 3px #535353, 45px 105px 0 3px #535353,
    50px 105px 0 3px #535353, 45px 110px 0 3px #535353, 50px 110px 0 3px #535353,
    55px 110px 0 3px #535353;
}
}
body {
background: #eee;
overflow: hidden;
}
body .t-rex {
position: absolute;
left: 50%;
top: 70%;
margin-left: 22px;
z-index: 1;
-webkit-animation: run 0.35s infinite;
-moz-animation: run 0.35s infinite;
-o-animation: run 0.35s infinite;
animation: run 0.35s infinite;
-webkit-animation-timing-function: linear;
animation-timing-function: linear;
}
body .eye {
position: absolute;
left: 50%;
top: 70%;
margin-left: 22px;
z-index: 1;
-webkit-animation: blinking 3.85s infinite;
-moz-animation: blinking 3.85s infinite;
-o-animation: blinking 3.85s infinite;
animation: blinking 3.85s infinite;
-webkit-animation-timing-function: linear;
animation-timing-function: linear;
}
body .horizont {
position: absolute;
left: 50%;
top: 70%;
margin-left: 22px;
z-index: -1;
box-shadow: -1000px 85px 0 3px #535353, -995px 85px 0 3px #535353, -990px 85px 0 3px #535353,
    -985px 85px 0 3px #535353, -980px 85px 0 3px #535353, -975px 85px 0 3px #535353,
    -970px 85px 0 3px #535353, -965px 85px 0 3px #535353, -960px 85px 0 3px #535353,
    -955px 85px 0 3px #535353, -950px 85px 0 3px #535353, -945px 85px 0 3px #535353,
    -940px 85px 0 3px #535353, -935px 85px 0 3px #535353, -930px 85px 0 3px #535353,
    -925px 85px 0 3px #535353, -920px 85px 0 3px #535353, -915px 85px 0 3px #535353,
    -910px 85px 0 3px #535353, -905px 85px 0 3px #535353, -900px 85px 0 3px #535353,
    -895px 85px 0 3px #535353, -890px 85px 0 3px #535353, -885px 85px 0 3px #535353,
    -880px 85px 0 3px #535353, -875px 85px 0 3px #535353, -870px 85px 0 3px #535353,
    -865px 85px 0 3px #535353, -860px 85px 0 3px #535353, -855px 85px 0 3px #535353,
    -850px 85px 0 3px #535353, -845px 85px 0 3px #535353, -840px 85px 0 3px #535353,
    -835px 85px 0 3px #535353, -830px 85px 0 3px #535353, -825px 85px 0 3px #535353,
    -820px 85px 0 3px #535353, -815px 85px 0 3px #535353, -810px 85px 0 3px #535353,
    -805px 85px 0 3px #535353, -800px 85px 0 3px #535353, -795px 85px 0 3px #535353,
    -790px 85px 0 3px #535353, -785px 85px 0 3px #535353, -780px 85px 0 3px #535353,
    -775px 85px 0 3px #535353, -770px 85px 0 3px #535353, -765px 85px 0 3px #535353,
    -760px 85px 0 3px #535353, -755px 85px 0 3px #535353, -750px 85px 0 3px #535353,
    -745px 85px 0 3px #535353, -740px 85px 0 3px #535353, -735px 85px 0 3px #535353,
    -730px 85px 0 3px #535353, -725px 85px 0 3px #535353, -720px 85px 0 3px #535353,
    -715px 85px 0 3px #535353, -710px 85px 0 3px #535353, -705px 85px 0 3px #535353,
    -700px 85px 0 3px #535353, -695px 85px 0 3px #535353, -690px 85px 0 3px #535353,
    -685px 85px 0 3px #535353, -680px 85px 0 3px #535353, -675px 85px 0 3px #535353,
    -670px 85px 0 3px #535353, -665px 85px 0 3px #535353, -660px 85px 0 3px #535353,
    -655px 85px 0 3px #535353, -650px 85px 0 3px #535353, -645px 85px 0 3px #535353,
    -640px 85px 0 3px #535353, -635px 85px 0 3px #535353, -630px 85px 0 3px #535353,
    -625px 85px 0 3px #535353, -620px 85px 0 3px #535353, -615px 85px 0 3px #535353,
    -610px 85px 0 3px #535353, -605px 85px 0 3px #535353, -600px 85px 0 3px #535353,
    -595px 85px 0 3px #535353, -590px 85px 0 3px #535353, -585px 85px 0 3px #535353,
    -580px 85px 0 3px #535353, -575px 85px 0 3px #535353, -570px 85px 0 3px #535353,
    -565px 85px 0 3px #535353, -560px 85px 0 3px #535353, -555px 85px 0 3px #535353,
    -550px 85px 0 3px #535353, -545px 85px 0 3px #535353, -540px 85px 0 3px #535353,
    -535px 85px 0 3px #535353, -530px 85px 0 3px #535353, -525px 85px 0 3px #535353,
    -520px 85px 0 3px #535353, -515px 85px 0 3px #535353, -510px 85px 0 3px #535353,
    -505px 85px 0 3px #535353, -500px 85px 0 3px #535353, -495px 85px 0 3px #535353,
    -490px 85px 0 3px #535353, -485px 85px 0 3px #535353, -480px 85px 0 3px #535353,
    -475px 85px 0 3px #535353, -470px 85px 0 3px #535353, -465px 85px 0 3px #535353,
    -460px 85px 0 3px #535353, -455px 85px 0 3px #535353, -450px 85px 0 3px #535353,
    -445px 85px 0 3px #535353, -440px 85px 0 3px #535353, -435px 85px 0 3px #535353,
    -430px 85px 0 3px #535353, -425px 85px 0 3px #535353, -420px 85px 0 3px #535353,
    -415px 85px 0 3px #535353, -410px 85px 0 3px #535353, -405px 85px 0 3px #535353,
    -400px 85px 0 3px #535353, -395px 85px 0 3px #535353, -390px 85px 0 3px #535353,
    -385px 85px 0 3px #535353, -380px 85px 0 3px #535353, -375px 85px 0 3px #535353,
    -370px 85px 0 3px #535353, -365px 85px 0 3px #535353, -360px 85px 0 3px #535353,
    -355px 85px 0 3px #535353, -350px 85px 0 3px #535353, -345px 85px 0 3px #535353,
    -340px 85px 0 3px #535353, -335px 85px 0 3px #535353, -330px 85px 0 3px #535353,
    -325px 85px 0 3px #535353, -320px 85px 0 3px #535353, -315px 85px 0 3px #535353,
    -310px 85px 0 3px #535353, -305px 85px 0 3px #535353, -300px 85px 0 3px #535353,
    -295px 85px 0 3px #535353, -290px 85px 0 3px #535353, -285px 85px 0 3px #535353,
    -280px 85px 0 3px #535353, -275px 85px 0 3px #535353, -270px 85px 0 3px #535353,
    -265px 85px 0 3px #535353, -260px 85px 0 3px #535353, -255px 85px 0 3px #535353,
    -250px 85px 0 3px #535353, -245px 85px 0 3px #535353, -240px 85px 0 3px #535353,
    -235px 85px 0 3px #535353, -230px 85px 0 3px #535353, -225px 85px 0 3px #535353,
    -220px 85px 0 3px #535353, -215px 85px 0 3px #535353, -210px 85px 0 3px #535353,
    -205px 85px 0 3px #535353, -200px 85px 0 3px #535353, -195px 85px 0 3px #535353,
    -190px 85px 0 3px #535353, -185px 85px 0 3px #535353, -180px 85px 0 3px #535353,
    -175px 85px 0 3px #535353, -170px 85px 0 3px #535353, -165px 85px 0 3px #535353,
    -160px 85px 0 3px #535353, -155px 85px 0 3px #535353, -150px 85px 0 3px #535353,
    -145px 85px 0 3px #535353, -140px 85px 0 3px #535353, -135px 85px 0 3px #535353,
    -130px 85px 0 3px #535353, -125px 85px 0 3px #535353, -120px 85px 0 3px #535353,
    -115px 85px 0 3px #535353, -110px 85px 0 3px #535353, -105px 85px 0 3px #535353,
    -100px 85px 0 3px #535353, -95px 85px 0 3px #535353, -90px 85px 0 3px #535353,
    -85px 85px 0 3px #535353, -80px 85px 0 3px #535353, -75px 85px 0 3px #535353,
    -70px 85px 0 3px #535353, -65px 85px 0 3px #535353, -60px 85px 0 3px #535353,
    -55px 85px 0 3px #535353, 5px 85px 0 3px #535353, 10px 85px 0 3px #535353,
    15px 85px 0 3px #535353, 20px 85px 0 3px #535353, 25px 85px 0 3px #535353,
    30px 85px 0 3px #535353, 35px 85px 0 3px #535353, 40px 85px 0 3px #535353,
    45px 85px 0 3px #535353, 50px 85px 0 3px #535353, 55px 85px 0 3px #535353,
    60px 85px 0 3px #535353, 65px 85px 0 3px #535353, 70px 85px 0 3px #535353,
    75px 85px 0 3px #535353, 80px 85px 0 3px #535353, 85px 85px 0 3px #535353,
    90px 85px 0 3px #535353, 95px 85px 0 3px #535353, 100px 85px 0 3px #535353,
    105px 85px 0 3px #535353, 110px 85px 0 3px #535353, 115px 85px 0 3px #535353,
    120px 85px 0 3px #535353, 125px 85px 0 3px #535353, 130px 85px 0 3px #535353,
    135px 85px 0 3px #535353, 140px 85px 0 3px #535353, 145px 85px 0 3px #535353,
    150px 85px 0 3px #535353, 155px 85px 0 3px #535353, 160px 85px 0 3px #535353,
    165px 85px 0 3px #535353, 170px 85px 0 3px #535353, 175px 85px 0 3px #535353,
    180px 85px 0 3px #535353, 185px 85px 0 3px #535353, 190px 85px 0 3px #535353,
    195px 85px 0 3px #535353, 200px 85px 0 3px #535353, 205px 85px 0 3px #535353,
    210px 85px 0 3px #535353, 215px 85px 0 3px #535353, 220px 85px 0 3px #535353,
    225px 85px 0 3px #535353, 230px 85px 0 3px #535353, 235px 85px 0 3px #535353,
    240px 85px 0 3px #535353, 245px 85px 0 3px #535353, 250px 85px 0 3px #535353,
    255px 85px 0 3px #535353, 260px 85px 0 3px #535353, 265px 85px 0 3px #535353,
    270px 85px 0 3px #535353, 275px 85px 0 3px #535353, 280px 85px 0 3px #535353,
    285px 85px 0 3px #535353, 290px 85px 0 3px #535353, 295px 85px 0 3px #535353,
    300px 85px 0 3px #535353, 305px 85px 0 3px #535353, 310px 85px 0 3px #535353,
    315px 85px 0 3px #535353, 320px 85px 0 3px #535353, 325px 85px 0 3px #535353,
    330px 85px 0 3px #535353, 335px 85px 0 3px #535353, 340px 85px 0 3px #535353,
    345px 85px 0 3px #535353, 350px 85px 0 3px #535353, 355px 85px 0 3px #535353,
    360px 85px 0 3px #535353, 365px 85px 0 3px #535353, 370px 85px 0 3px #535353,
    375px 85px 0 3px #535353, 380px 85px 0 3px #535353, 385px 85px 0 3px #535353,
    390px 85px 0 3px #535353, 395px 85px 0 3px #535353, 400px 85px 0 3px #535353,
    405px 85px 0 3px #535353, 410px 85px 0 3px #535353, 415px 85px 0 3px #535353,
    420px 85px 0 3px #535353, 425px 85px 0 3px #535353, 430px 85px 0 3px #535353,
    435px 85px 0 3px #535353, 440px 85px 0 3px #535353, 445px 85px 0 3px #535353,
    450px 85px 0 3px #535353, 455px 85px 0 3px #535353, 460px 85px 0 3px #535353,
    465px 85px 0 3px #535353, 470px 85px 0 3px #535353, 475px 85px 0 3px #535353,
    480px 85px 0 3px #535353, 485px 85px 0 3px #535353, 490px 85px 0 3px #535353,
    495px 85px 0 3px #535353, 500px 85px 0 3px #535353, 505px 85px 0 3px #535353,
    510px 85px 0 3px #535353, 515px 85px 0 3px #535353, 520px 85px 0 3px #535353,
    525px 85px 0 3px #535353, 530px 85px 0 3px #535353, 535px 85px 0 3px #535353,
    540px 85px 0 3px #535353, 545px 85px 0 3px #535353, 550px 85px 0 3px #535353,
    555px 85px 0 3px #535353, 560px 85px 0 3px #535353, 565px 85px 0 3px #535353,
    570px 85px 0 3px #535353, 575px 85px 0 3px #535353, 580px 85px 0 3px #535353,
    585px 85px 0 3px #535353, 590px 85px 0 3px #535353, 595px 85px 0 3px #535353,
    600px 85px 0 3px #535353, 605px 85px 0 3px #535353, 610px 85px 0 3px #535353,
    615px 85px 0 3px #535353, 620px 85px 0 3px #535353, 625px 85px 0 3px #535353,
    630px 85px 0 3px #535353, 635px 85px 0 3px #535353, 640px 85px 0 3px #535353,
    645px 85px 0 3px #535353, 650px 85px 0 3px #535353, 655px 85px 0 3px #535353,
    660px 85px 0 3px #535353, 665px 85px 0 3px #535353, 670px 85px 0 3px #535353,
    675px 85px 0 3px #535353, 680px 85px 0 3px #535353, 685px 85px 0 3px #535353,
    690px 85px 0 3px #535353, 695px 85px 0 3px #535353, 700px 85px 0 3px #535353,
    705px 85px 0 3px #535353, 710px 85px 0 3px #535353, 715px 85px 0 3px #535353,
    720px 85px 0 3px #535353, 725px 85px 0 3px #535353, 730px 85px 0 3px #535353,
    735px 85px 0 3px #535353, 740px 85px 0 3px #535353, 745px 85px 0 3px #535353,
    750px 85px 0 3px #535353, 755px 85px 0 3px #535353, 760px 85px 0 3px #535353,
    765px 85px 0 3px #535353, 770px 85px 0 3px #535353, 775px 85px 0 3px #535353,
    780px 85px 0 3px #535353, 785px 85px 0 3px #535353, 790px 85px 0 3px #535353,
    795px 85px 0 3px #535353, 800px 85px 0 3px #535353, 805px 85px 0 3px #535353,
    810px 85px 0 3px #535353, 815px 85px 0 3px #535353, 820px 85px 0 3px #535353,
    825px 85px 0 3px #535353, 830px 85px 0 3px #535353, 835px 85px 0 3px #535353,
    840px 85px 0 3px #535353, 845px 85px 0 3px #535353, 850px 85px 0 3px #535353,
    855px 85px 0 3px #535353, 860px 85px 0 3px #535353, 865px 85px 0 3px #535353,
    870px 85px 0 3px #535353, 875px 85px 0 3px #535353, 880px 85px 0 3px #535353,
    885px 85px 0 3px #535353, 890px 85px 0 3px #535353, 895px 85px 0 3px #535353,
    900px 85px 0 3px #535353, 905px 85px 0 3px #535353, 910px 85px 0 3px #535353,
    915px 85px 0 3px #535353, 920px 85px 0 3px #535353, 925px 85px 0 3px #535353,
    930px 85px 0 3px #535353, 935px 85px 0 3px #535353, 940px 85px 0 3px #535353,
    945px 85px 0 3px #535353, 950px 85px 0 3px #535353;
}
body .mountain,
body .mountainSec,
body .mountainThrd {
position: absolute;
top: 70%;
z-index: 0;
box-shadow: 0px 85px 0 3px #eee, 5px 85px 0 3px #eee, 10px 85px 0 3px #eee, 15px 85px 0 3px #eee,
    20px 85px 0 3px #eee, 25px 85px 0 3px #eee, 30px 85px 0 3px #eee, 35px 85px 0 3px #eee,
    40px 85px 0 3px #eee, 45px 85px 0 3px #eee, 50px 85px 0 3px #eee, 55px 85px 0 3px #eee,
    -5px 80px 0 3px #535353, 0px 80px 0 3px #535353, 0px 75px 0 3px #535353, 5px 75px 0 3px #535353,
    10px 75px 0 3px #535353, 10px 70px 0 3px #535353, 15px 70px 0 3px #535353,
    15px 65px 0 3px #535353, 20px 65px 0 3px #535353, 25px 65px 0 3px #535353,
    30px 65px 0 3px #535353, 35px 65px 0 3px #535353, 40px 65px 0 3px #535353,
    40px 70px 0 3px #535353, 45px 75px 0 3px #535353, 50px 75px 0 3px #535353,
    55px 80px 0 3px #535353;
-webkit-animation: move 6.35s infinite;
-moz-animation: move 6.35s infinite;
-o-animation: move 6.35s infinite;
animation: move 6.35s infinite;
-webkit-animation-timing-function: linear;
animation-timing-function: linear;
}
body .mountainSec {
margin-left: 250px;
}
body .mountainThrd {
margin-left: 900px;
}
body .cloud,
body .cloudSec,
body .cloudThrd {
position: absolute;
top: 35%;
z-index: -1;
box-shadow: 0px 0px 0 3px #939393, 5px 0px 0 3px #939393, 50px 0px 0 3px #939393,
    55px 0px 0 3px #939393, 60px 0px 0 3px #939393, 65px 0px 0 3px #939393, 70px 0px 0 3px #939393,
    75px 0px 0 3px #939393, 80px 0px 0 3px #939393, 85px 0px 0 3px #939393, 90px 0px 0 3px #939393,
    95px 0px 0 3px #939393, 100px 0px 0 3px #939393, 105px 0px 0 3px #939393,
    110px 0px 0 3px #939393, 115px 0px 0 3px #939393, 120px 0px 0 3px #939393,
    125px 0px 0 3px #939393, 130px 0px 0 3px #939393, 135px 0px 0 3px #939393,
    140px 0px 0 3px #939393, 145px 0px 0 3px #939393, 150px 0px 0 3px #939393,
    155px 0px 0 3px #939393, 160px 0px 0 3px #939393, 165px 0px 0 3px #939393,
    170px 0px 0 3px #939393, 175px 0px 0 3px #939393, 180px 0px 0 3px #939393,
    185px 0px 0 3px #939393, 190px 0px 0 3px #939393, 195px 0px 0 3px #939393,
    200px 0px 0 3px #939393, 205px 0px 0 3px #939393, 210px 0px 0 3px #939393,
    215px 0px 0 3px #939393, 220px 0px 0 3px #939393, 225px 0px 0 3px #939393,
    230px 0px 0 3px #939393, 235px 0px 0 3px #939393, 5px -5px 0 3px #939393,
    10px -5px 0 3px #939393, 20px -5px 0 3px #939393, 25px -5px 0 3px #939393,
    25px -10px 0 3px #939393, 25px -15px 0 3px #939393, 30px -15px 0 3px #939393,
    30px -20px 0 3px #939393, 35px -20px 0 3px #939393, 40px -20px 0 3px #939393,
    45px -20px 0 3px #939393, 50px -20px 0 3px #939393, 55px -20px 0 3px #939393,
    60px -20px 0 3px #939393, 65px -20px 0 3px #939393, 70px -20px 0 3px #939393,
    70px -25px 0 3px #939393, 75px -25px 0 3px #939393, 75px -30px 0 3px #939393,
    80px -30px 0 3px #939393, 85px -30px 0 3px #939393, 90px -30px 0 3px #939393,
    90px -35px 0 3px #939393, 90px -40px 0 3px #939393, 90px -45px 0 3px #939393,
    95px -45px 0 3px #939393, 100px -45px 0 3px #939393, 100px -50px 0 3px #939393,
    105px -50px 0 3px #939393, 105px -55px 0 3px #939393, 110px -55px 0 3px #939393,
    115px -55px 0 3px #939393, 120px -55px 0 3px #939393, 125px -55px 0 3px #939393,
    130px -55px 0 3px #939393, 135px -55px 0 3px #939393, 140px -55px 0 3px #939393,
    140px -60px 0 3px #939393, 145px -60px 0 3px #939393, 150px -60px 0 3px #939393,
    155px -60px 0 3px #939393, 160px -60px 0 3px #939393, 160px -55px 0 3px #939393,
    165px -55px 0 3px #939393, 170px -55px 0 3px #939393, 170px -50px 0 3px #939393,
    175px -50px 0 3px #939393, 175px -45px 0 3px #939393, 175px -40px 0 3px #939393,
    180px -40px 0 3px #939393, 185px -40px 0 3px #939393, 185px -35px 0 3px #939393,
    190px -35px 0 3px #939393, 195px -35px 0 3px #939393, 200px -35px 0 3px #939393,
    205px -35px 0 3px #939393, 210px -35px 0 3px #939393, 210px -30px 0 3px #939393,
    210px -25px 0 3px #939393, 215px -25px 0 3px #939393, 220px -25px 0 3px #939393,
    225px -25px 0 3px #939393, 225px -20px 0 3px #939393, 225px -15px 0 3px #939393,
    230px -15px 0 3px #939393, 235px -15px 0 3px #939393, 240px -15px 0 3px #939393,
    240px -10px 0 3px #939393, 240px -5px 0 3px #939393;
-webkit-animation: move 35.35s infinite;
-moz-animation: move 35.35s infinite;
-o-animation: move 35.35s infinite;
animation: move 35.35s infinite;
-webkit-animation-timing-function: linear;
animation-timing-function: linear;
}
body .cloudSec {
margin-left: 200px;
margin-top: 90px;
}
body .cloudThrd {
margin-left: 600px;
margin-top: 45px;
}
body .pteroBox {
position: absolute;
top: 27%;
left: 50%;
z-index: 0;
-webkit-animation: move 10.35s infinite;
-moz-animation: move 10.35s infinite;
-o-animation: move 10.35s infinite;
animation: move 10.35s infinite;
-webkit-animation-timing-function: linear;
animation-timing-function: linear;
}
body .pteroBox .ptero {
-webkit-animation: ptero 0.7s infinite;
-moz-animation: ptero 0.7s infinite;
-o-animation: ptero 0.7s infinite;
animation: ptero 0.7s infinite;
-webkit-animation-timing-function: linear;
animation-timing-function: linear;
}
</style>
  
