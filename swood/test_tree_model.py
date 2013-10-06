#! /usr/bin/env python

# Copyright 2011 Tom SF Haines

# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.



from dec_tree import DecTree
import test_model as mod



# A full decision tree test, with many categories, weights and both discrete and continuous attributes, using the model defined in test_model...



# Get trainning data...
int_dm, real_dm, cats, weights = mod.generate_train()



# Train...
dt = DecTree(int_dm, real_dm, cats, weights)



# Test...
mod.test(dt.classify)
