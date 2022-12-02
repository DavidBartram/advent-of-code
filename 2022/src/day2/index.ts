import { pipe } from "fp-ts/lib/function";
import { Day } from "../day";
import * as A from "fp-ts/Array";

class Day2 extends Day {
  constructor() {
    super(2);
  }

  solveForPartOne(input: string): string {
    const getResult = (moves: {
      theirMove: 0 | 1 | 2;
      myMove: 0 | 1 | 2;
    }): 0 | 3 | 6 => {
      var result: 0 | 3 | 6 = 0;

      if (moves.theirMove === moves.myMove) {
        result = 3;
      }

      if (moves.myMove === (moves.theirMove + 1) % 3) {
        result = 6;
      }

      return result;
    };

    const moveLookup: Record<string, 0 | 1 | 2> = {
      A: 0,
      B: 1,
      C: 2,
      X: 0,
      Y: 1,
      Z: 2,
    };

    return pipe(
      input.split("\n"),
      A.map((x) => {
        const s = x.split(" ");
        const moves = { theirMove: moveLookup[s[0]], myMove: moveLookup[s[1]] };
        const score = getResult(moves) + moves.myMove + 1;
        return score;
      }),
      A.reduce(0, (acc, n) => acc + n),
      (x) => x.toString()
    );
  }

  solveForPartTwo(input: string): string {
    const theirMoveLookup: Record<string, 0 | 1 | 2> = {
      A: 0,
      B: 1,
      C: 2,
    };

    const resultLookup: Record<string, 0 | 3 | 6> = {
      X: 0,
      Y: 3,
      Z: 6,
    };

    const getMyMove = (moves: {
      theirMove: 0 | 1 | 2;
      result: 0 | 3 | 6;
    }): number => {
      var myMove: number = 0;

      switch (moves.result) {
        case 3:
          myMove = moves.theirMove;
          break;
        case 0:
          myMove = (moves.theirMove + 2) % 3;
          break;
        case 6:
          myMove = (moves.theirMove + 1) % 3;
          break;
      }

      return myMove;
    };

    return pipe(
      input.split("\n"),
      A.map((x) => {
        const s = x.split(" ");
        const moves = {
          theirMove: theirMoveLookup[s[0]],
          result: resultLookup[s[1]],
        };
        return moves.result + getMyMove(moves) + 1;
      }),
      A.reduce(0, (acc, n) => acc + n),
      (x) => x.toString()
    );
  }
}

export default new Day2();
