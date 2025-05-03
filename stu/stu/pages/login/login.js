const request = require('../../utils/request.js');

Page({
  formSubmit: function(e) {
    const { email, password } = e.detail.value;
    
    if (!email || !password) {
      wx.showToast({
        title: '请填写所有字段',
        icon: 'none'
      });
      return;
    }
    const param = {
      email:email,
      password:password
    }
    request.post("/login", param)
      .then(res => {
        console.log(res)
        if (res.code === 200) {
          wx.showToast({
            title: '登录成功',
            icon: 'success'
          });
          wx.setStorageSync('userInfo', res.data);
          setTimeout(() => {
            wx.reLaunch({ url: '/pages/index/index' });
          }, 1500);
        } else {
          wx.showToast({
            title: res.message || '登录失败',
            icon: 'none'
          });
        }
      })
      .catch(err => {
        wx.showToast({
          title: '用户密码有误',
          icon: 'none'
        });
      });
  }
});