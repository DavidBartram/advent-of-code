import { Day } from "../day";
import * as A from "fp-ts/Array";
import { pipe, flow } from "fp-ts/lib/function";
import { showNumber } from "fp-ts/lib/Show";

class Day1 extends Day {
  constructor() {
    super(1);
  }

  solveForPartOne(input: string): string {
    return pipe(
      input,
      (x) => x.split("\n\n"),
      A.map((x) => x.split("\n")),
      A.map(
        flow(
          A.map((x) => Number(x)),
          A.reduce(0, (acc, num) => acc + num)
        )
      ),
      (x) => Math.max(...x).toString()
    );
  }

  solveForPartTwo(input: string): string {
    return pipe(
      input,
      (x) => x.split("\n\n"),
      A.map((x) => x.split("\n")),
      A.map(
        flow(
          A.map((x) => Number(x)),
          A.reduce(0, (acc, num) => acc + num)
        )
      ),
      (x) => x.sort((a, b) => b - a),
      (x) => (x[0] + x[1] + x[2]).toString()
    );
  }
}

export default new Day1();
