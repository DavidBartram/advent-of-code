import { Day } from "../day";
import * as A from "fp-ts/Array";
import { pipe, flow } from "fp-ts/lib/function";
import { right } from "fp-ts/lib/Separated";
import { Set } from "immutable";
import { setFlagsFromString } from "v8";

class Day3 extends Day {
  constructor() {
    super(3);
  }

  spliceArrayIntoChunks(
    arr: Array<string>,
    chunkSize: number
  ): Array<Array<string>> {
    const res = [];
    while (arr.length > 0) {
      const chunk = arr.splice(0, chunkSize);
      res.push(chunk);
    }
    return res;
  }

  solveForPartOne(input: string): string {
    return pipe(
      input,
      (x) => x.split("\n"),
      A.map((x) => {
        const mid = x.length / 2;
        return { left: Set(x.slice(0, mid)), right: Set(x.slice(mid)) };
      }),
      A.map((x) => x.left.intersect(x.right).first("")),
      A.reduce(0, (acc, char) => {
        if (char === char.toUpperCase()) {
          return acc + char.charCodeAt(0) - 38;
        } else {
          return acc + char.charCodeAt(0) - 96;
        }
      }),
      (x) => x.toString()
    );
  }

  solveForPartTwo(input: string): string {
    return pipe(
      input,
      (x) => this.spliceArrayIntoChunks(x.split("\n"), 3),
      A.map((x) => ({ left: Set(x[0]), middle: Set(x[1]), right: Set(x[2]) })),
      A.map((x) => x.left.intersect(x.middle).intersect(x.right).first("")),
      A.reduce(0, (acc, char) => {
        if (char === char.toUpperCase()) {
          return acc + char.charCodeAt(0) - 38;
        } else {
          return acc + char.charCodeAt(0) - 96;
        }
      }),
      (x) => x.toString()
    );
  }
}

export default new Day3();
