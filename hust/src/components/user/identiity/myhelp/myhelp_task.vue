<template>
  <div class="task">
            <header>我的任务</header>
        <hr>
        <div id="opt">
        <table border=1>
            <td><input type="button" value="已发布" > </td>
            <td><input type="button" value="已接受" ></td>
            <td><input type="button" value="未付款" ></td>
            <td><input type="button" value="已付款" ></td>
        </table>
        </div>
        <hr>
        <div id="show" > 
        <table border=1>
            <tr>
                <td width="15%"><img src="" alt="图片" ></td>
            <td width="40%">任务内容</td>
            <td width="30%" ><t>距现在时间为</t></td>
            <td width="15%"><input type="button" value="详情"></td>
            </tr>
            <tr>
                <td width="15%"><img src="" alt="图片" ></td>
            <td width="40%">任务内容</td>
            <td width="30%">距现在时间为</td>
            <td width="15%"><input type="button" value="详情"></td>
            </tr>
        </table>
        </div>
  </div>
</template>

<script>
export default {

}
</script>

<style type="text/css" scoped>
       #opt table{
               font-size: 20px;
               text-align: center;
               margin: 0px auto;
               width: 80%;
               height: 54px;
        }
        header{
                font-size: 50px;
                background-color: lightskyblue;
        }   
        input{
            width: 100%;
            height: 100%;
            background-color: rgb(255, 255, 255);
        }
        #show table{
            width: 100%;
            text-align: left;
            position: relative;
            font-size:18px;
            min-height: 160px;
            border:1px ;
        }
        #show input{
            position: relative;
            width: 60%;
            font-size: 14px;
            height: 60%;
        }
        t{
            position: relative;
            bottom:0%;
            text-align: right;
        }
        </style> 