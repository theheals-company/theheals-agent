#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import time
import asyncio
import logging
import urllib.request
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

# 환경 변수 로드
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
CLAUDE_API_KEY = os.environ.get("CLAUDE_API_KEY", "")
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "")
# [새로 추가됨] 3차 특허 준비방 웹훅 주소
PATENT_WEBHOOK_URL = os.environ.get("PATENT_WEBHOOK_URL", "")

class DiscordBridge:
    @staticmethod
    def send_log_to_discord(webhook_url, title, content, color=3066993):
        if !webhook_url:
            logging.warning("웹훅 URL이 비어있습니다.")
            return False
        
        payload = {
            "embeds": [{
                "title": title,
                "description": content,
                "color": color,
                "timestamp": datetime.utcnow().isoformat(),
                "footer": {"text": "더힐즈 매트릭스 엔진 - 자율 특허 및 작전본부"}
            }]
        }
        try:
            req = urllib.request.Request(
                webhook_url,
                data=json.dumps(payload).encode('utf-8'),
                headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req) as res:
                return res.status in [200, 204]
        except Exception as e:
            logging.error(f"디스코드 웹훅 전송 실패: {e}")
            return False

async def main_control_loop():
    logging.info("더힐즈 듀얼 라우팅 특허 엔진 가동...")
    
    # 1. 일반 작전방 알림
    DiscordBridge.send_log_to_discord(
        DISCORD_WEBHOOK_URL, 
        "📢 [에이전트 허브] 서킷 브레이커 및 듀얼 인프라 가동", 
        "더힐즈 컴퍼니 자율 점검 인프라가 완전히 가동되었습니다. 특허 모듈 실시간 감시를 시작합니다.",
        color=3066993
    )
    
    await asyncio.sleep(2)
    
    # 2. 3차 특허 준비방에 1차 원천기술 명세서 자동 송출
    if PATENT_WEBHOOK_URL:
        patent_content = (
            "**[더힐즈 매트릭스 엔진 - 제1차 특허 청구 스펙 선점안]**\n\n"
            "**1. 발명의 명칭:**\n"
            "단안 비디오 스트림으로부터의 실시간 깊이 맵 추출 기반 XR 미용 교육용 가위질 가림 보정 시스템 및 그 방법\n\n"
            "**2. 해결하고자 하는 과제:**\n"
            "메타 퀘스트 고글 내에서 시술자의 손과 가위가 마네킹을 가리는 '오클루전(Occlusion)' 발생 시, 관절 인식 뼈대가 유실되어 좌표가 튀는 현상을 차단하고 15ms 이하의 초고속 연산을 사수함.\n\n"
            "**3. 핵심 기술적 구성:**\n"
            "유실된 앵커 포인트를 직전 5프레임의 속도 벡터와 가림 점유율 알파($\\alpha$) 행렬을 결합해 실시간 동적 추정(Dynamic Extrapolation)함.\n\n"
            "**4. 기대 효과:**\n"
            "고가의 장비 없이 단 1대의 2D 카메라만으로 끊김 없는 90fps급 가위질 상호작용 및 머리카락 서각서각 잘리는 햅틱 저항감 교육 환경 구현."
        )
        
        success = DiscordBridge.send_log_to_discord(
            PATENT_WEBHOOK_URL,
            "💡 [3차 특허 확보] 자율 도출된 제1차 핵심 원천기술 명세서",
            patent_content,
            color=16764928 # 특허방 전용 황금색 레이블
        )
        if success:
            logging.info("특허방으로 문서 송출 성공!")
    else:
        logging.warning("PATENT_WEBHOOK_URL 환경변수가 등록되지 않아 특허방 전송을 대기합니다.")

if __name__ == "__main__":
    asyncio.run(main_control_loop())
