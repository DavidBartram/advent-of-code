"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
const function_1 = require("fp-ts/lib/function");
const day_1 = require("../day");
const A = __importStar(require("fp-ts/Array"));
class Day2 extends day_1.Day {
    constructor() {
        super(2);
    }
    solveForPartOne(input) {
        const getResult = (moves) => {
            var result = 0;
            if (moves.theirMove === moves.myMove) {
                result = 3;
            }
            if (moves.myMove === (moves.theirMove + 1) % 3) {
                result = 6;
            }
            return result;
        };
        const moveLookup = {
            A: 0,
            B: 1,
            C: 2,
            X: 0,
            Y: 1,
            Z: 2,
        };
        return (0, function_1.pipe)(input.split("\n"), A.map((x) => {
            const s = x.split(" ");
            const moves = { theirMove: moveLookup[s[0]], myMove: moveLookup[s[1]] };
            const score = getResult(moves) + moves.myMove + 1;
            return score;
        }), A.reduce(0, (acc, n) => acc + n), (x) => x.toString());
    }
    solveForPartTwo(input) {
        const theirMoveLookup = {
            A: 0,
            B: 1,
            C: 2,
        };
        const resultLookup = {
            X: 0,
            Y: 3,
            Z: 6,
        };
        const getMyMove = (moves) => {
            var myMove = 0;
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
        return (0, function_1.pipe)(input.split("\n"), A.map((x) => {
            const s = x.split(" ");
            const moves = {
                theirMove: theirMoveLookup[s[0]],
                result: resultLookup[s[1]],
            };
            return moves.result + getMyMove(moves) + 1;
        }), A.reduce(0, (acc, n) => acc + n), (x) => x.toString());
    }
}
exports.default = new Day2();
