# -*- coding: utf-8 -*-
"""基于仓库扫描器封面生成代理人自动培养封面（管线同 disc_cleanup）"""
from PIL import Image, ImageDraw, ImageFont
import os

SRC = r"/workspace\plugins-src\zzzod-plugin-inventory-scan\inventory_scan\assets\ui\cover.png"
DST = r"/workspace\plugins-src\zzzod-plugin-agent-train\agent_train\assets\ui\cover.png"

CYAN = (63, 224, 208)
GRAY = (168, 185, 190)
WHITE = (240, 246, 247)

im = Image.open(SRC).convert("RGBA")
W, H = im.size  # 600x376

# ---- 1) 抹掉左侧原文字区：逐列上下取样垂直插值 + 羽化 ----
x0, y0, x1, y1 = 30, 58, 332, 254
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = overlay.load()
FEATHER = 22
for x in range(x0, x1):
    tp = im.getpixel((x, max(y0 - 7, 0)))
    bp = im.getpixel((x, min(y1 + 7, H - 1)))
    for y in range(y0, y1):
        t = (y - y0) / (y1 - y0)
        r = int(tp[0] + (bp[0] - tp[0]) * t)
        g = int(tp[1] + (bp[1] - tp[1]) * t)
        b = int(tp[2] + (bp[2] - tp[2]) * t)
        a = 255
        if x - x0 < FEATHER:
            a = int(255 * (x - x0) / FEATHER)
        elif x1 - 1 - x < FEATHER:
            a = int(255 * (x1 - 1 - x) / FEATHER)
        ay = a
        if y - y0 < FEATHER:
            ay = min(ay, int(a * (y - y0) / FEATHER))
        elif y1 - 1 - y < FEATHER:
            ay = min(ay, int(a * (y1 - 1 - y) / FEATHER))
        od[x, y] = (r, g, b, ay)
im = Image.alpha_composite(im, overlay)

draw = ImageDraw.Draw(im)

# ---- 2) 新标题文字 ----
def font(path, size, index=0):
    try:
        return ImageFont.truetype(path, size, index=index)
    except Exception:
        return ImageFont.load_default()

ARIAL = r"C:\Windows\Fonts\arialbd.ttf"
MSYH = r"C:\Windows\Fonts\msyhbd.ttc"
if not os.path.exists(MSYH):
    MSYH = r"C:\Windows\Fonts\msyh.ttc"

f1 = font(ARIAL, 46)
f_sub = font(MSYH, 22)
f_badge = font(MSYH, 17)

draw.text((42, 62), "AGENT", font=f1, fill=WHITE)
draw.text((42, 112), "TRAIN", font=f1, fill=CYAN)
draw.text((43, 170), "代理人自动培养", font=f_sub, fill=GRAY)

# ---- 3) 徽章 ----
def badge(x, y, text):
    tw = draw.textlength(text, font=f_badge)
    pad_x, pad_y = 11, 6
    bx0, by0 = x, y
    bx1, by1 = x + tw + pad_x * 2, y + 17 + pad_y * 2
    draw.rounded_rectangle([bx0, by0, bx1, by1], radius=9, outline=CYAN, width=2)
    draw.text((bx0 + pad_x, by0 + pad_y - 1), text, font=f_badge, fill=CYAN)
    return bx1

bx = badge(42, 212, "白名单制")
badge(bx + 14, 212, "皇冠保护")

# ---- 4) 徽章：游戏内「养成指南」logo，右侧圆环右下角 ----
LOGO_SRC = r"~\.workbuddy\clipboard-images\clipboard-2026-11-05T01-25-09-959Z-3bd4c4ee.jpg"
cx, cy, S = 512, 292, 84  # 徽章中心与边长
logo = Image.open(LOGO_SRC).convert("RGB")
# 以白框中心 (92,103) 为中心取方形裁剪（含黑色圆角方底）
half = 82
logo = logo.crop((92 - half, 103 - half, 92 + half, 103 + half)).resize((S, S), Image.LANCZOS)
# 圆角遮罩
mask = Image.new("L", (S, S), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, S - 1, S - 1], radius=14, fill=255)
im.paste(logo, (cx - S // 2, cy - S // 2), mask)
draw.rounded_rectangle([cx - S // 2, cy - S // 2, cx + S // 2 - 1, cy + S // 2 - 1],
                       radius=14, outline=CYAN, width=3)
draw.ellipse([cx - 48, cy - 48, cx + 48, cy + 48], outline=(63, 224, 208, 90), width=1)

os.makedirs(os.path.dirname(DST), exist_ok=True)
im.convert("RGB").save(DST)
print("saved", DST, im.size)
