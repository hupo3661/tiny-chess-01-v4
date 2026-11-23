# tiny-chess-01 — 4KB chess engine

A compact Python chess engine built for the make.fun **tiny-chess-01** contest
(program/v1 protocol). The whole engine ships as a single self-extracting
`main.py` of **4,074 bytes** (limit: 4,096), produced by the official kit's
`compress` command from the source in `src/engine2.py`.

## Design

- 0x88 board, pseudo-legal move generation with make/unmake legality checks
- Iterative-deepening alpha-beta (PVS) with a transposition table
- Quiescence search (captures + check evasions, depth-capped) using a fast
  material+PST evaluation; full tapered (PeSTO-style) evaluation with
  mobility, rook open-file and passed-pawn terms in the main search
- Repetition avoidance with contempt: a won position is steered away from
  threefold repetitions, a lost one toward them
- Fixed node budget per move (70,000 nodes) — pure node counting, no clock,
  no randomness: games replay byte-for-byte

## Files

- `main.py` — the compressed, submittable engine (kit compress output)
- `src/engine2.py` — the readable source it was compressed from
- `LICENSE` — MIT

## Protocol

The engine reads `MAKEFUN_ENV_URL` from the environment, opens a game with
`POST /game`, and answers each `your_move` state with `POST /move` (UCI move),
following `next_game` until the match ends.
