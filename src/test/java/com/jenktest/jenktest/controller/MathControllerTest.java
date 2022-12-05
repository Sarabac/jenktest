package com.jenktest.jenktest.controller;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class MathControllerTest {

    @Autowired
    MathController mathController;

    @Test
    void testSum() {
        int a = 4;
        int b = 5;
        assertEquals(9, mathController.sum(a, b));

    }
    @Test
    void testSumFail() {
        int a = 5;
        int b = 5;
        assertEquals(9, mathController.sum(a, b));

    }
}
