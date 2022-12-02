import day2 from "./index";

describe("On Day 2", () => {
  it(`part1 example`, () => {
    expect(day2.solveForPartOne("A Y\nB X\nC Z")).toBe("15");
  });
});

describe("On Day 2", () => {
  it(`part2 their example`, () => {
    expect(day2.solveForPartTwo("A Y\nB X\nC Z")).toBe("12");
  });
});

describe("On Day 2", () => {
  it(`part2 my example`, () => {
    expect(day2.solveForPartTwo("A Z\nC X\nB Z")).toBe("19");
  });
});
