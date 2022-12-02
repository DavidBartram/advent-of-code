import day1 from "./index";

describe("On Day 1", () => {
  it(`part1 example`, () => {
    expect(
      day1.solveForPartOne(
        "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
      )
    ).toBe("24000");
  });
});

describe("On Day 1", () => {
  it(`part2 example`, () => {
    expect(
      day1.solveForPartTwo(
        "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
      )
    ).toBe("45000");
  });
});
