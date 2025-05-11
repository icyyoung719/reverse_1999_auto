def ocr_postprocess(text: str) -> str:
    """OCR结果后处理（示例函数）"""
    return text.strip().replace(' ', '')


def get_game_state() -> dict:
    """获取当前游戏状态（示例函数）"""
    return {"is_battle": False, "current_scene": "home"}