export type LabeledFaceDescriptor = {
  label: string;
  descriptor: number[];
};

// FaceMatcher class
export default class FaceMatcher {
  private labeledDescriptors: LabeledFaceDescriptor[];
  private threshold: number;

  constructor(labeledDescriptors: LabeledFaceDescriptor[], threshold: number = 0.6) {
    this.labeledDescriptors = labeledDescriptors;
    this.threshold = threshold;
  }

  public euclideanDistance(descriptor1: number[], descriptor2: number[]): number {
    if (descriptor1.length !== descriptor2.length) {
      throw new Error("Descriptors must have the same length");
    }
    let sum = 0;
    for (let i = 0; i < descriptor1.length; i++) {
      const diff = descriptor1[i] - descriptor2[i];
      sum += diff * diff;
    }
    return Math.sqrt(sum);
  }

  public findBestMatch(queryDescriptor: number[]): { label: string; distance: number } {
    let bestMatch = { label: "unknown", distance: Infinity };

    for (const labeledDescriptor of this.labeledDescriptors) {
      const distance = this.euclideanDistance(labeledDescriptor.descriptor, queryDescriptor);

      if (distance < bestMatch.distance && distance < this.threshold) {
        bestMatch = { label: labeledDescriptor.label, distance };
      }
    }

    return bestMatch;
  }
}
