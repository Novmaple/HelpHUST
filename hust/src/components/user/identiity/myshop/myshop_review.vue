<template>
  <div class="review">
<div id="head0">
    <h1>我的评价
</h1>
</div>
    <div id="head2">
        <table border="2">
            <td><form> 
                <input type="button" value="已完成" style="height:40px;width:100px; ">
            </form></td><td><form> 
                <input type="button" value="未完成" style="height:40px;width:100px;  ">
            </form></td>
        </table>
        </div>

    <table border="big">
        <tr class="one">
            <th width="13%" height="80px" style="font-size:150%;">购买时间</th>
            <th width="13%" style="font-size:150%;">商品名称</th>
            <th width="13%" style="font-size:150%;">所属店铺</th>
            <th width="20%" style="font-size:150%;">商品描述</th>
            <th width="20%" style="font-size:150%;">商品价格</th>
            <th width="34%" style="font-size:150%;">我的评价</th>
        </tr>
       
        <tr>
            <td  height="80px">2021-05-07</td>
            <td>王小波《我的精神家园》</td>
            <td>中文系小甜甜</td>
            <td>全新无痕迹，便宜出</td>
            <td>原价20r 优惠15r 二手价5r</td>
            <td><img src="https://img14.360buyimg.com/pop/jfs/t1/37014/15/15403/98574/60064686Ee5d3be98/a248b640a811c653.jpg" 
                style="width:10%;height:10%"
                alt="打开失败">
                学姐人好好，买了好几本书了，便宜又干净！</td>
            
        </tr>
        <tr>
            <td height="80px">2021-07-05</td>
            <td>美工刀</td>
            <td>西四楼实验狗</td>
            <td>便宜出美工刀啊，全新的</td>
            <td>原价3r 优惠2r 二手价1r</td>
            <td>去学长实验室拿的，学长人很好，小刀确实是全新的，拆快递很方便</td>
           
        </tr>
        <tr>
            <td height="80px">…… </td>
            <td> </td>
            <td> </td>
            <td>  </td>
            <td>  </td>
            <td>  </td>
           
        </tr>
        <tr>
            <td height="40px">…… </td>
            <td> </td>
            <td> </td>
            <td>  </td>
            <td>  </td>
            <td>  </td>
    
        </tr>
    </table>
    <div id="head1">
        <p style="text-align: center;">
         Hust.帮
        </p> 
     </div>
    </div>
</template>

<script>
export default {};
</script>

<style scoped>
#head0 {
  background-color: rgb(240, 230, 230);
  color: rgb(37, 4, 4);
  border: 1px solid rgb(26, 6, 6);
  height: 80px;
}
#head1 {
  background-color: rgb(43, 3, 3);
  color: white;
  border: 1px solid rgb(26, 6, 6);
  text-align: center;
  margin-top: 1%;
  height: 50px;
}
#head2 {
  height: 80px;
  text-align: center;
}
.caption {
  text-align: center;
  font-family: "宋体";
  font-size: 200%;
  font-weight: 1000;
  letter-spacing: 20px;
}
#time {
  font-weight: 300px;
}
.slow {
  text-align: right;
  color: blue;
}
#slowy {
  text-align: right;
  color: blue;
}
table {
  font-size: 16px;
  text-align: center;
  margin: 3px auto;
  width: 60%;
}
</style>