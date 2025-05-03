import json
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder


class ApiResponse(JsonResponse):
    """
    统一 API 响应格式
    """

    def __init__(self, code=200, message="成功", data=None, status=200, extra=None, **kwargs):
        """
        :param code: 业务状态码（默认200）
        :param message: 响应消息（默认"成功"）
        :param data: 返回的数据（默认None）
        :param status: HTTP 状态码（默认200）
        :param extra: 额外附加字段（默认None）
        :param kwargs: 其他参数
        """
        response_data = {
            "code": code,
            "message": message,
            "data": data if data is not None else {},
        }

        if extra:
            response_data.update(extra)

        # 记录 API 响应日志
        # logger.info(f"API Response: {json.dumps(response_data, ensure_ascii=False)}")

        # 这里只传递字典类型的参数
        super().__init__(
            response_data,
            status=status,
            json_dumps_params={"ensure_ascii": False},  # 确保不重复传递 cls
            **kwargs
        )

    @classmethod
    def success(cls, data=None, message="成功", extra=None):
        """成功响应"""
        return cls(code=200, message=message, data=data, status=200, extra=extra)

    @classmethod
    def error(cls, message="失败", code=400, status=400, extra=None):
        """错误响应"""
        return cls(code=code, message=message, status=status, extra=extra)

    @classmethod
    def not_found(cls, message="资源未找到"):
        """404 响应"""
        return cls.error(message=message, code=404, status=404)

    @classmethod
    def forbidden(cls, message="没有权限"):
        """403 响应"""
        return cls.error(message=message, code=403, status=403)

    @classmethod
    def unauthorized(cls, message="未认证"):
        """401 响应"""
        return cls.error(message=message, code=401, status=401)

    @classmethod
    def paginated(cls, queryset, page=1, page_size=10, serializer=None):
        """分页响应"""
        paginator = Paginator(queryset, page_size)
        try:
            paginated_data = paginator.page(page)
        except EmptyPage:
            return cls.error(message="页码超出范围", code=400)

        if serializer:
            data = serializer(paginated_data, many=True).data
        else:
            data = list(paginated_data)

        response_data = {
            "total": paginator.count,
            "total_pages": paginator.num_pages,
            "current_page": page,
            "page_size": page_size,
            "data": data
        }

        return cls.success(response_data)
