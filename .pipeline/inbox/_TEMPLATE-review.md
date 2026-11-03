---
auto: review
workdir: .pipeline/redacted/<이름>
prompt: .pipeline/redacted/<이름>/prompt.md
output: docs/review/<이름>-result.md
redacted: true
---
# <리뷰 요청 제목>

Codex가 읽기 전용으로 1회만 검토합니다. 코드 작성·worktree·병합은 하지 않습니다.

- **Codex에는 이름을 가린 비식별 사본만 보냅니다(v0.5.0).** `workdir:` 폴더에 대상 파일 사본과 지시문을 두고 고객사·인명·제품명·미공개 수치를 가린 뒤 `redacted: true`를 적으세요. 둘 중 하나라도 없으면 Codex를 부르지 않고 실패로 알립니다.
- `prompt:` 지시문 파일(리뷰할 대상과 관점)을 `workdir` 안에 먼저 만들어 두세요. 없으면 Codex를 부르지 않고 실패로 알립니다.
- `output:` 결과가 저장될 파일입니다. 이미 있으면 `.bak-날짜`로 백업한 뒤 새로 씁니다.
- 모두 이 프로젝트 폴더 기준 상대 경로입니다.
- 선택 항목(머리말에 추가): `max_attempts: 4`(한도 시 총 시도 횟수) · `retry_delay_sec: 600`(재시도 간격) · `rerun: true`(같은 내용을 일부러 다시 돌릴 때)
- 성공하면 이 요청서는 접수함에서 자동으로 지워집니다. 지시문과 결과 파일은 지워지지 않습니다.
