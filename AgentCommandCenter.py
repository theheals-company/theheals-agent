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

# 환경 변수 로드 (3원화 안테나 완벽 매핑)
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "")
PATENT_WEBHOOK_URL = os.environ.get("PATENT_WEBHOOK_URL", "")
NEW_BIZ_WEBHOOK_URL = os.environ.get("NEW_BIZ_WEBHOOK_URL", "")

class DiscordBridge:
    @staticmethod
    def send_log_to_discord(webhook_url, title, content, color=3066993):
        if not webhook_url:  # [교정 완료] !에서 not으로 문법 수정
            logging.warning("웹훅 URL이 비어있습니다.")
            return False
        
        payload = {
            "embeds": [{
                "title": title,
                "description": content,
                "color": color,
                "timestamp": datetime.utcnow().isoformat(),
                "footer": {"text": "더힐즈 매트릭스 엔진 - 3원화 자율 지휘소"}
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
    logging.info("더힐즈 컴퍼니 3원화 라우팅 독립 엔진 가동 시스템 시동...")
    
    # 채널 1: 기존 작전방 송출
    if DISCORD_WEBHOOK_URL:
        DiscordBridge.send_log_to_discord(
            DISCORD_WEBHOOK_URL, 
            "📢 [에이전트 허브] 3원화 인프라 최종 개통 성공", 
            "더힐즈 컴퍼니 자율 점검 인프라가 3원화 체제로 업그레이드 완료되었습니다.\n- 본부 작전방: 관제 중\n- 3차 특허방: 감시 중\n- 신사업 기획방: 대기 중",
            color=3066993
        )
    
    await asyncio.sleep(1)
    
    # 채널 2: 3차 특허 준비방 송출
    if PATENT_WEBHOOK_URL:
        patent_content = (
            "**[더힐즈 매트릭스 엔진 - 제1차 특허 청구 스펙 선점안]**\n\n"
            "**1. 발명의 명칭:**\n"
            "단안 비디오 스트림으로부터의 실시간 깊이 맵 추출 기반 XR 미용 교육용 가위질 가림 보정 시스템 및 그 방법\n\n"
            "**2. 해결하고자 하는 과제:**\n"
            "메타 퀘스트 내 가위질 중 발생되는 오클루전 시, 관절 인식 유실 좌표 튐 현상을 차단하고 15ms 이하 연산을 사수함.\n\n"
            "**3. 핵심 기술적 구성:**\n"
            "유실 앵커 포인트를 속도 벡터와 가림 점유율 알파($\\alpha$) 행렬로 실시간 동적 추정(Dynamic Extrapolation)함."
        )
        DiscordBridge.send_log_to_discord(
            PATENT_WEBHOOK_URL,
            "💡 [3차 특허 확보] 자율 도출된 제1차 핵심 원천기술 명세서",
            patent_content,
            color=16764928 # 황금색 레이블
        )

    await asyncio.sleep(1)

    # 채널 3: 신규 사업 기획방 송출
    if NEW_BIZ_WEBHOOK_URL:
        new_biz_content = (
            "🚀 **[신규 비즈니스 인프라] 독자 기획 채널 개통**\n\n"
            "본 채널은 더힐즈 미용 XR R&D와 분리된 완전히 새로운 신규 사업 아이디어, "
            "시장 분석 데이터, BM 기획서 전용 격리 저장소입니다.\n"
            "대표님의 지시가 떨어지는 즉시 전용 에이전트가 가동됩니다."
        )
        DiscordBridge.send_log_to_discord(
            NEW_BIZ_WEBHOOK_URL,
            "✨ [신규 사업] 3원화 독립 기획방 연동 성공",
            new_biz_content,
            color=1752220 # 푸른색 레이블
        )

if __name__ == "__main__":
    asyncio.run(main_control_loop())
