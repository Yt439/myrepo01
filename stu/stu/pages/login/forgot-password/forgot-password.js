Page({
  formSubmit: function(e) {
    const { email } = e.detail.value;
    
    if (!email) {
      wx.showToast({
        title: '请输入邮箱',
        icon: 'none'
      });
      return;
    }

    // 这里应该调用后端API发送重置密码邮件
    // 示例中使用模拟数据
    wx.showToast({
      title: '重置邮件已发送',
      icon: 'success'
    });
  }
});