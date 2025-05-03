const request = require('../../../utils/request.js');

Page({
  formSubmit: function(e) {
    const { email, username, password, confirmPassword } = e.detail.value;
    
    // 简单的表单验证
    if (!email || !password || !username || !confirmPassword) {
      wx.showToast({
        title: '请填写所有字段',
        icon: 'none'
      });
      return;
    }

    if (password !== confirmPassword) {
      wx.showToast({
        title: '两次密码不一致',
        icon: 'none'
      });
      return;
    }

    // 准备请求参数
    const param = {
      email,
      username,
      password
    };

    // 发送注册请求
    request.post("/register", param)
      .then(res => {
        if (res.code === 200) { // 假设200表示成功，根据你的实际接口返回调整
          wx.showToast({
            title: '注册成功',
            icon: 'success'
          });

          // 注册成功后跳转到登录页面
          setTimeout(() => {
            wx.navigateTo({ url: '/pages/login/login' });
          }, 1500);
        } else {
          wx.showToast({
            title: res.message || '注册失败',
            icon: 'none'
          });
        }
      })
      .catch(err => {
        // 处理网络错误或其他异常
        wx.showToast({
          title: err.message || '网络错误，请稍后重试',
          icon: 'none'
        });
        console.error('注册失败:', err);
      });
  }
});