package com.jenktest.jenktest.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/math")
public class MathController {

    private static final int constant = 0;

    @GetMapping("/sum/{a}/{b}")
    public Integer sum(@PathVariable("a") final int a, @PathVariable("b") final int b) {
        
        return a + b + constant;
    }

}
