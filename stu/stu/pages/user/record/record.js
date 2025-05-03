// pages/user/record/record.js
const request = require('../../../utils/request.js');
Page({

  /**
   * 页面的初始数据
   */
  data: {
    records: [],
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onShow(options) {
    this.findUser();
  },

  findUser(){
    const userInfo = wx.getStorageSync('userInfo');
    param = {
      user_id:userInfo.id
    }
    request.post("/findAnswers", param)
      .then(res => {
        console.log(res.data)
        this.setData({
          records:res.data.data
        })
      })
      .catch(err => {
      });
  },

  goToDetail(e) {
    const number = e.currentTarget.dataset.number;
    wx.navigateTo({
      url: `/pages/user/jilu/jilu?number=${number}`,
    });
  }
  

})