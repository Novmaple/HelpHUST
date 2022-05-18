<template>
  <div class="goods_ask">
<div class="body">

   <div class="line-1"  id="Theme">
        <div class="text">
            商品名称：
        </div>
        <div class="input">
            <input class="h0" type="text" placeholder=
              "请输入商品名称">
        </div>
   </div>

    <div class="line-2">
        <div class="text">
            商品描述：
        </div>
        <div class="input">
            <textarea class="h1" ></textarea>  
        </div>  
    </div>

    <div class="line-1">
        <div class="text">
            商品价格：
        </div>
        <div class="input">
            <input class="h2" type="tel" placeholder=
            "请输入商品价格" >
        </div> 
    </div>

    <div class="line-1">
        <div class="text">
            联系方式：
        </div>
        <div class="input">
            <input class="h2" type="tel" placeholder=
            "请输入您的联系方式" >   
        </div>
    </div>

    <div class="line-2">
        <div class="text">
            &nbsp;备&nbsp;&nbsp;&nbsp;&nbsp;注&nbsp;：
        </div>
        <div class="input">
            <textarea class="h1"></textarea>    
        </div>
    </div>

    <div class="line-1">
        <div class="text">
        </div>
        <div class="input">
            <input class="h3" type="button"  value="提交">
        </div>
    </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
.line-1{
    height:80px;
    display: flex;
    justify-content: center;
    position: relative;
    top:50px;
}

.line-2{
    height:105px;
    display: flex;
    justify-content: center;
    position: relative;
    top:50px;
}
.text{
      width:100px;
      font-family: "黑体";
      font-size: 105%;
      position:relative;
      top:20px;

}
.input{
      position:relative;
      top:20px;
}

.h0{
    width: 250px;
    height: 30px;
    border:1px solid dodgerblue;
    border-radius: 3px 3px 3px 3px ;
}
.h1{
    width: 600px;
    height: 50px;
    border:1px solid dodgerblue;
    border-radius: 3px 3px 3px 3px ;
}
.h2{
    width: 600px;
    height: 25px;
    border:1px solid dodgerblue;
    border-radius: 3px 3px 3px 3px ;
}
.h3{
    width: 60px;
    height: 35px;
    font-size: 105%;
    color:floralwhite;
    background-color: deepskyblue;
    border:1px solid deepskyblue;
    border-radius: 5px 5px 5px 5px ;
}
</style>