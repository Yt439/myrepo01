Component({
  data: {
    active: 0, // 默认选中的 tab
  },
  methods: {
    onTabChange(event) {
      const { name } = event.detail;
      const newActive = parseInt(name, 10);

      if (this.data.active === newActive) return;

      this.setData({
        active: newActive,
      });

      // 其他逻辑（可选）
    },
  },
});