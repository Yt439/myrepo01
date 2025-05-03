const BASE_URL = 'http://localhost:8000'; // 你的后端接口地址

const request = (url, method, data = {}, header = {}) => {
  return new Promise((resolve, reject) => {
    wx.request({
      url: BASE_URL + url,
      method: method,
      data: data,
      header: {
        'Content-Type': 'application/json',
        'Authorization': wx.getStorageSync('token') || '', // 读取存储的 token
        ...header,
      },
      success: (res) => {
        if (res.statusCode === 200) {
          resolve(res.data);
        } else {
          wx.showToast({
            title: res.data.message || '请求失败',
            icon: 'none',
          });
          reject(res);
        }
      },
      fail: (err) => {
        wx.showToast({
          title: '网络异常，请稍后重试',
          icon: 'none',
        });
        reject(err);
      },
    });
  });
};

const get = (url, data = {}, header = {}) => {
  return request(url, 'GET', data, header);
};

const post = (url, data = {}, header = {}) => {
  return request(url, 'POST', data, header);
};

const put = (url, data = {}, header = {}) => {
  return request(url, 'PUT', data, header);
};

const del = (url, data = {}, header = {}) => {
  return request(url, 'DELETE', data, header);
};

module.exports = {
  get,
  post,
  put,
  del,
};
