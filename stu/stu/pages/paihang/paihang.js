
const request = require('../../utils/request.js');
Page({
  data: {
    rankList: [],
    isModalVisible: false, 
    selectedUser: {}
  },

  onShow: function () {
    this.getRankData();
  },

  getRankData() {
    request.post("/findpaihang")
      .then(res => {
        this.setData({
          rankList:res.data.data
        })
        console.log()
      })
      .catch(err => {
      });

  },

  showDetails(e) {
    const index = e.currentTarget.dataset.index;
    console.log(index)
    const user = this.data.rankList[index];
    console.log(user)
    this.setData({
      isModalVisible: true,
      selectedUser: index
    });
  },

  // 关闭弹出框
  closeModal() {
    this.setData({
      isModalVisible: false
    });
  },
})
